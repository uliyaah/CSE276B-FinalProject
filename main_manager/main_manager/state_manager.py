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
        
        # Define valid states
        self.valid_states = {"IDLE", "SENTRY", "INTERVENTION_1", "INTERVENTION_2", "INTERVENTION_3", "PAUSED"}
        
        # State publisher (so Main Manager knows current state)
        self.state_publisher = self.create_publisher(String, 'state_manager/state', 10)
        
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
        
        # Emit output commands based on new state
        self.emit_output_commands(new_state)

    def emit_output_commands(self, state: str):
        """
        Emit commands to output managers based on new state.
        TODO: Implement actual command emission to Movement, Display, Speaker managers.
        For now, just log what would be sent.
        """
        self.get_logger().info(f'[TODO] Emitting output commands for state: {state}')
        
        # Placeholder for future implementation
        # if state == "INTERVENTION_1":
        #     self.send_to_movement_manager("...")
        #     self.send_to_display_manager("...")
        #     self.send_to_speaker_manager("...")

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
