########
# Name: state_manager.py
#
# Purpose: State Manager - FSM for pupper behavior.
#          Receives commands from Main Manager and coordinates output managers.
#          Publishes state transitions so Main Manager and other nodes stay in sync.
#
# States: IDLE, SENTRY, INTERVENTION_1, INTERVENTION_2, INTERVENTION_3, PAUSED, CELEBRATE
#
# Date: 01 June 2026
########

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

from pupper_interfaces.srv import StateManagerCommand
from pupper_interfaces.msg import Command
from pupper_behaviors.behaviors import (
    IdleBehavior,
    SentryBehavior,
    Intervention1Behavior,
    Intervention2Behavior,
    Intervention3Behavior,
    PausedBehavior,
    CelebrateBehavior
)


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
    - CELEBRATE: 50-minute milestone celebration
    
    Publishes state changes so Main Manager knows current state.
    """

    def __init__(self):
        super().__init__('state_manager')

        # FSM state
        self.current_state = "IDLE"
        self.state_before_pause = None  # Track state to return to when unpausing
        
        # Track robot position: "move_away" (origin) or "approach" (close to user)
        self.robot_position = "move_away"
        
        # Define valid states
        self.valid_states = {"IDLE", "SENTRY", "INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3", "PAUSED", "CELEBRATE"}
        
        # State publisher (so Main Manager knows current state)
        self.state_publisher = self.create_publisher(String, 'state_manager/state', 10)
        
        # Movement publisher (to Movement Manager)
        self.movement_publisher = self.create_publisher(String, 'movement/command', 10)
        
        # Display publisher (to Display Manager)
        self.display_publisher = self.create_publisher(String, 'display/command', 10)
        
        # Speaker publisher (to Speaker Manager)
        self.speaker_publisher = self.create_publisher(String, 'speaker/command', 10)
        
        # Service server for commands from Main Manager
        self.command_service = self.create_service(
            StateManagerCommand,
            'state_manager_command',
            self.handle_command
        )
        
        self.get_logger().info(f'State Manager initialized in state: {self.current_state}')
        self.publish_state()

    def handle_command(self, request, response):
        """
        Handle incoming command from Main Manager.
        Parse command string and trigger state transition.
        """
        command_str = request.command.command
        
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
            # Touch event - state-aware behavior
            if command == "activate_pupper":
                if self.current_state in ["SENTRY", "INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
                    # Save current state before pausing
                    self.state_before_pause = self.current_state
                    self.transition_to("PAUSED")
                elif self.current_state == "IDLE":
                    # Start monitoring from idle
                    self.transition_to("SENTRY")
                elif self.current_state == "PAUSED":
                    # Resume to the previous state
                    if self.state_before_pause:
                        self.transition_to(self.state_before_pause)
                        self.state_before_pause = None
                    else:
                        # Fallback to SENTRY if no previous state recorded
                        self.transition_to("SENTRY")
                # Else in CELEBRATE, ignore
                return True
            
            # Distraction events
            elif command == "distraction_low":
                if self.current_state == "SENTRY":
                    self.transition_to("INTERVENTION_1")
                return True
            
            elif command == "distraction_medium":
                if self.current_state == "INTERVENTION_1":
                    self.transition_to("INTERVENTION_2")
                return True
            
            elif command == "distraction_high":
                if self.current_state == "INTERVENTION_2":
                    self.transition_to("INTERVENTION_3")
                return True
            
            elif command == "distraction_ended":
                # Return to SENTRY from intervention states
                if self.current_state in ["SENTRY","INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
                    self.transition_to("SENTRY")
                return True
            
            elif command == "celebrate":
                # Transition to CELEBRATE from any state
                self.transition_to("CELEBRATE")
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
        - Returning to SENTRY from INTERVENTION requires "move_away" (return to origin)
        - INTERVENTION_1 stays in place (no approach)
        """
    
        # Check if new state requires shake
        if new_state in ["INTERVENTION_1", "CELEBRATE"]:
            msg = String()
            msg.data = "shake"
            self.movement_publisher.publish(msg)
            self.get_logger().info(f'Movement command: shake')

        # Check if new state requires approach
        elif new_state == "INTERVENTION_2":
            msg = String()
            msg.data = "approach"
            self.movement_publisher.publish(msg)
            self.robot_position = "approach"
            self.get_logger().info(f'Movement command: approach')       
        elif new_state == "INTERVENTION_3":
            msg = String()
            msg.data = "beg"
            self.movement_publisher.publish(msg)
            self.robot_position = "approach_beg"
            self.get_logger().info(f'Movement command: approach_beg')
        
        # Check if returning to SENTRY requires moving back
        elif new_state == "SENTRY" and old_state in ["INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3"]:
            if self.robot_position != "move_away":
                msg = String()
                msg.data = "move_away"
                self.movement_publisher.publish(msg)
                self.robot_position = "move_away"
                self.get_logger().info(f'Movement command: move_away')
        
        # CELEBRATE is a milestone - stay in place
        # INTERVENTION_1 doesn't require approach, just stays in place
        # IDLE, PAUSED don't affect movement position

    def emit_output_commands(self, state: str):
        """
        Emit commands to output managers based on new state.
        Publishes to movement, display, and speaker managers.
        """
        behavior_commands = None
        
        # Get behavior for this state
        if state == "IDLE":
            behavior_commands = IdleBehavior.get_all_commands()
        elif state == "SENTRY":
            behavior_commands = SentryBehavior.get_all_commands()
        elif state == "INTERVENTION_1":
            behavior_commands = Intervention1Behavior.get_all_commands()
        elif state == "INTERVENTION_2":
            behavior_commands = Intervention2Behavior.get_all_commands()
        elif state == "INTERVENTION_3":
            behavior_commands = Intervention3Behavior.get_all_commands()
        elif state == "PAUSED":
            behavior_commands = PausedBehavior.get_all_commands()
        elif state == "CELEBRATE":
            behavior_commands = CelebrateBehavior.get_all_commands()
        
        if behavior_commands:
            self.get_logger().info(
                f'Emitting behavior commands for {state}:\n'
                f'  Movement: {behavior_commands["movement"]}\n'
                f'  Display: {behavior_commands["display"]}\n'
                f'  Speaker: {behavior_commands["speaker"]}'
            )
            
            # Publish movement command
            movement_msg = String()
            movement_msg.data = json.dumps(behavior_commands["movement"])
            self.movement_publisher.publish(movement_msg)
            
            # Publish display command
            display_msg = String()
            display_msg.data = json.dumps(behavior_commands["display"])
            self.display_publisher.publish(display_msg)
            
            # Publish speaker command
            speaker_msg = String()
            speaker_msg.data = json.dumps(behavior_commands["speaker"])
            self.speaker_publisher.publish(speaker_msg)

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
