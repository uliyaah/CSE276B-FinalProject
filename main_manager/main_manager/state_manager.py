########
# Name: state_manager.py
#
# Purpose: State Manager - FSM for pupper behavior.
#          Receives commands from Main Manager and coordinates output managers.
#          Publishes state transitions so Main Manager and other nodes stay in sync.
#
# States: IDLE, SENTRY, INTERVENTION_1, INTERVENTION_2, INTERVENTION_3, PAUSED
#
# Date: 01 June 2026
########

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pupper_interfaces.srv import StateManagerCommand
from pupper_interfaces.msg import Command
from pupper_behaviors.behaviors import IdleBehavior, SentryBehavior


class StateManager(Node):
    """
    State Manager FSM that routes commands to output managers.
    
    States:
    - IDLE: Waiting for activation
    - SENTRY: Active, watching for distraction
    - INTERVENTION_1: Responding to low distraction
    - INTERVENTION_2: Responding to medium distraction
    - INTERVENTION_3: Responding to high distraction
    - PAUSED: Paused by user touch
    
    Publishes state changes so Main Manager knows current state.
    """

    def __init__(self):
        super().__init__('state_manager')

        # FSM state
        self.current_state = "IDLE"
        
        # Track robot position: "back" (origin) or "approach" (close to user)
        self.robot_position = "back"
        
        # Define valid states
        self.valid_states = {"IDLE", "SENTRY", "INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3", "PAUSED"}
        
        # State publisher (so Main Manager knows current state)
        self.state_publisher = self.create_publisher(String, 'state_manager/state', 10)
        
        # Movement publisher (to Movement Manager)
        self.movement_publisher = self.create_publisher(String, 'movement/command', 10)
        
        # Service server for commands from Main Manager
        self.command_service = self.create_service(
            StateManagerCommand,
            'state_manager_command',
            self.handle_command
        )
        
        # TODO: Create clients/publishers for output managers (Movement, Display, Speaker)
        # For now, just stubs for logging
        
        self.get_logger().info(f'State Manager initialized in state: {self.current_state}')
        self.publish_state()

    def handle_command(self, request, response):
        """
        Handle incoming command from Main Manager.
        Parse command string and trigger state transition.
        """
        command_str = request.command.command
        self.get_logger().info(f'Received command: {command_str}')
        
        # Dispatch command to transition logic
        success = self.process_command(command_str)
        
        response.success = success
        return response

    def process_command(self, command: str) -> bool:
        """
        Process command and transition state accordingly.
        
        Commands from Main Manager:
        - "activate_pupper" (touch on front)
        - "distraction_low"
        - "distraction_medium"
        - "distraction_high"
        - "distraction_ended"
        
        Note: Proximity detection (walk_towards, walk_away) is handled
        by Main Manager publishing to movement/command topic directly.
        """
        try:
            # Touch event - always go to PAUSED
            if command == "activate_pupper":
                if self.current_state in ["SENTRY", "INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
                    self.transition_to("PAUSED")
                elif self.current_state == "IDLE":
                    self.transition_to("SENTRY")
                # Else in PAUSED, ignore (user already paused)
                return True
            
            # Distraction events
            elif command == "distraction_low":
                if self.current_state == "SENTRY":
                    self.transition_to("INTERVENTION_1")
                return True
            
            elif command == "distraction_medium":
                if self.current_state == "SENTRY":
                    self.transition_to("INTERVENTION_2")
                elif self.current_state == "INTERVENTION_1":
                    self.transition_to("INTERVENTION_2")
                return True
            
            elif command == "distraction_high":
                # Always escalate to INTERVENTION_3
                if self.current_state in ["SENTRY", "INTERVENTION_1", "INTERVENTION_2"]:
                    self.transition_to("INTERVENTION_3")
                return True
            
            elif command == "distraction_ended":
                # Return to SENTRY from intervention states
                if self.current_state in ["INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
                    self.transition_to("SENTRY")
                return True
            
            else:
                self.get_logger().warn(f'Unknown command: {command}')
                return False

        except Exception as e:
            self.get_logger().error(f'Error processing command: {e}')
            return False

    def transition_to(self, new_state: str):
        """Transition to a new state and emit output commands."""
        if new_state not in self.valid_states:
            self.get_logger().error(f'Invalid state: {new_state}')
            return
        
        old_state = self.current_state
        self.current_state = new_state
        
        self.get_logger().info(f'State transition: {old_state} -> {new_state}')
        
        # Publish state change
        self.publish_state()
        
        # Emit movement commands based on state transitions
        self.emit_movement_commands(old_state, new_state)
        
        # Emit output commands based on new state
        self.emit_output_commands(new_state)

    def emit_movement_commands(self, old_state: str, new_state: str):
        """
        Emit movement commands to Movement Manager based on state transitions.
        
        Rules:
        - INTERVENTION_2 and INTERVENTION_3 require "approach" (move fixed amount toward user)
        - Returning to SENTRY from INTERVENTION requires "back" (return to origin)
        - INTERVENTION_1 stays in place (no approach)
        """
        # Check if new state requires approach
        if new_state in ["INTERVENTION_2", "INTERVENTION_3"]:
            if self.robot_position != "approach":
                msg = String()
                msg.data = "approach"
                self.movement_publisher.publish(msg)
                self.robot_position = "approach"
                self.get_logger().info(f'Movement command: approach')
        
        # Check if returning to SENTRY requires moving back
        elif new_state == "SENTRY" and old_state in ["INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
            if self.robot_position != "back":
                msg = String()
                msg.data = "back"
                self.movement_publisher.publish(msg)
                self.robot_position = "back"
                self.get_logger().info(f'Movement command: back')
        
        # INTERVENTION_1 doesn't require approach, just stays in place
        # IDLE, PAUSED don't affect movement position

    def emit_output_commands(self, state: str):
        """
        Emit commands to output managers based on new state.
        Currently logs behavior commands. 
        TODO: Route to actual output managers.
        """
        behavior_commands = None
        
        # Get behavior for this state
        if state == "IDLE":
            behavior_commands = IdleBehavior.get_all_commands()
        elif state == "SENTRY":
            behavior_commands = SentryBehavior.get_all_commands()
        elif state in ["INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
            # TODO: Implement behavior classes for intervention states
            self.get_logger().info(f'[TODO] Behavior for {state} not yet implemented')
            return
        elif state == "PAUSED":
            # TODO: Implement behavior for PAUSED state
            self.get_logger().info(f'[TODO] Behavior for PAUSED not yet implemented')
            return
        
        if behavior_commands:
            self.get_logger().info(
                f'Emitting behavior commands for {state}:\n'
                f'  Movement: {behavior_commands["movement"]}\n'
                f'  Display: {behavior_commands["display"]}\n'
                f'  Speaker: {behavior_commands["speaker"]}'
            )
            # TODO: Actually send to Movement, Display, Speaker managers
            # self.send_to_movement_manager(behavior_commands["movement"])
            # self.send_to_display_manager(behavior_commands["display"])
            # self.send_to_speaker_manager(behavior_commands["speaker"])

    def publish_state(self):
        """Publish current state so other nodes can stay in sync."""
        msg = String()
        msg.data = self.current_state
        self.state_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    state_manager = StateManager()

    try:
        rclpy.spin(state_manager)
    except KeyboardInterrupt:
        state_manager.get_logger().info('Shutting down State Manager')
    finally:
        state_manager.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
