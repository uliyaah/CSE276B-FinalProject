########
# Name: main_manager.py
#
# Purpose: Main Manager node - Pure event router + session tracker.
#          Receives Distraction Event and Touch Event
#          Interprets them and forwards unified command to State Manager
#          Tracks distraction count for the session
#
# Date: 01 June 2026
########

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pupper_interfaces.msg import (
    DistractionEvent,
    TouchEvent,
    Command
)
from pupper_interfaces.srv import StateManagerCommand

from .session_tracker import SessionTracker


class MainManager(Node):
    """
    Main Manager node that routes events to State Manager.
    
    - Subscribes to distraction_event, touch_event topics
    - Interprets events based on configurable rules
    - Calls state_manager_command service with unified command
    - Tracks session metrics (distraction count, etc.)
    """

    def __init__(self):
        super().__init__('main_manager')

        # Initialize session tracker
        self.session_tracker = SessionTracker()

        # Create subscribers for the three event types
        self.distraction_sub = self.create_subscription(
            DistractionEvent,
            'distraction_event',
            self.distraction_callback,
            10
        )

        # Subscribe to touch events (published by input_detection)
        self.touch_sub = self.create_subscription(
            TouchEvent,
            'touch_event',
            self.touch_callback,
            10
        )

        # Subscribe to state manager state updates
        self.state_sub = self.create_subscription(
            String,
            'state_manager/state',
            self.on_state_update,
            10
        )

        # Create service client for State Manager
        self.state_manager_cli = self.create_client(
            StateManagerCommand,
            'state_manager_command'
        )

        # Wait for State Manager service to be available
        while not self.state_manager_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for state_manager_command service...')

        # State and configuration
        self.current_state = "idle"
        self.state_manager_state = "IDLE"  # Track state from State Manager
        self.current_distraction_level = None  # None, "low", "medium", "high"
        
        # Distraction escalation thresholds (in seconds)
        self.distraction_level_1_threshold = 2.0   # Delay before sending distraction_low
        self.distraction_level_2_threshold = 7.0   # Level 2 (medium): 5s from start
        self.distraction_level_3_threshold = 17.0  # Level 3 (high): 15s from start
        # Level 1 (low): starts after 2s delay
    

        # Timer to trigger celebrate state after 30 minutes
        self.celebrate_timer = self.create_timer(40.0, self.on_celebrate_timeout)

        self.get_logger().info(f'Main Manager initialized: Celebrate in 30 min')

    def distraction_callback(self, msg: DistractionEvent):
        """
        Handle distraction event with time-based escalation.
        
        Escalation schedule (based on distraction duration):
        - At 2s: Send distraction_low → INTERVENTION_1
        - At 5s: Send distraction_medium → INTERVENTION_2
        - At 15s: Send distraction_high → INTERVENTION_3
        - At end: Send distraction_ended → SENTRY
        """
        duration = msg.duration
        self.get_logger().info(f'duration: {duration}')
                
        # Handle premature distraction end
        if duration < 0:
            self.get_logger().info('Distraction ended')
            self.send_command("distraction_ended")
            return

        # Schedule distraction_high at 15 seconds if duration supports it
        elif duration > self.distraction_level_3_threshold:
            self.get_logger().info(f'Level 3: {self.current_distraction_level}')
            self._on_escalate_to_high()
        
        # Schedule distraction_medium at 5 seconds if duration supports it
        elif duration > self.distraction_level_2_threshold:
            self.get_logger().info(f'Level 2: {self.current_distraction_level}')
            self._on_escalate_to_medium()
            
        # New distraction - schedule escalation timers
        elif duration > self.distraction_level_1_threshold:
            self.get_logger().info(f'Level 1: {self.current_distraction_level}')
            self._on_escalate_to_low()
        
    
    def _on_escalate_to_low(self):
        """Escalate to low distraction level (INTERVENTION_1) after 2s delay."""
        
        self.current_distraction_level = "low"
        self.send_command("distraction_low")
        self.get_logger().info('Distraction escalated to low (INTERVENTION_1)')
    
    def _on_escalate_to_medium(self):
        """Escalate to medium distraction level (INTERVENTION_2)."""
        self.current_distraction_level = "medium"
        self.send_command("distraction_medium")
        self.get_logger().info('Distraction escalated to medium (INTERVENTION_2)')
    
    def _on_escalate_to_high(self):
        """Escalate to high distraction level (INTERVENTION_3)."""
        self.current_distraction_level = "high"
        self.send_command("distraction_high")
        self.get_logger().info('Distraction escalated to high (INTERVENTION_3)')
    
    def _on_distraction_end(self):
        """Distraction period ended, return to SENTRY."""
        self.get_logger().info('Distraction ended, returning to SENTRY')
        self.current_distraction_level = None
        self.send_command("distraction_ended")

    def touch_callback(self, msg: TouchEvent):
        """
        Handle touch event.
        
        Rule: touch on front -> "activate_pupper"
               State-aware interpretation:
               - In IDLE: start monitoring (IDLE -> SENTRY)
               - In SENTRY/INTERVENTION_1/2/3: pause (-> PAUSED)
               - In PAUSED: resume (PAUSED -> SENTRY)
              touch on left -> "reset_position"
        """
        location = msg.location

        # Interpret touch
        if location == "front":
            command_str = "activate_pupper"
            self.get_logger().info(
                f'Touch Event: {location} in state {self.state_manager_state} -> activate_pupper'
            )
            self.send_command(command_str)
        elif location == "left":
            command_str = "reset_position"
            self.get_logger().info(
                f'Touch Event: {location} in state {self.state_manager_state} -> reset_position'
            )
            self.send_command(command_str)
        else:
            # Log the touch but don't forward (context-dependent)
            self.get_logger().info(
                f'Touch Event: {location} -> no action (context-dependent)'
            )

        # Log the event for session tracking
        self.session_tracker.log_touch(location)

    def send_command(self, command_str: str):
        """
        Send a unified command to the State Manager service.
        
        Args:
            command_str: Command string (e.g., "activate_pupper", "user_nearby")
        """
        # Create request
        request = StateManagerCommand.Request()
        request.command = Command()
        request.command.command = command_str

        # Call service asynchronously
        future = self.state_manager_cli.call_async(request)
        future.add_done_callback(self.on_state_manager_response)

    def on_celebrate_timeout(self):
        """Called after 50 minutes - trigger celebrate state."""
        self.get_logger().info('50 minutes reached - triggering celebrate state')
        self.send_command('celebrate')

    def on_state_update(self, msg: String):
        """
        Handle state update from State Manager.
        Keep local copy in sync so we can make state-aware decisions.
        """
        self.state_manager_state = msg.data
        self.get_logger().debug(f'State Manager state: {self.state_manager_state}')

    def on_state_manager_response(self, future):
        """Handle response from State Manager service."""
        try:
            response = future.result()
            if response.success:
                self.get_logger().debug('State Manager accepted command')
            else:
                self.get_logger().warn('State Manager rejected command')
        except Exception as e:
            self.get_logger().error(f'State Manager call failed: {e}')


def main(args=None):
    rclpy.init(args=args)

    main_manager = MainManager()

    try:
        rclpy.spin(main_manager)
    except KeyboardInterrupt:
        main_manager.get_logger().info('Shutting down Main Manager')
    finally:
        # Cancel any pending timers
        if main_manager.celebrate_timer is not None:
            main_manager.celebrate_timer.cancel()
        main_manager.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
