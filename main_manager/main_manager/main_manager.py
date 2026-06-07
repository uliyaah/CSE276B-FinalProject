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
        self.distraction_level_1_threshold = 5.0   # Level 1 (low): 0-5s
        self.distraction_level_2_threshold = 15.0  # Level 2 (medium): 5-15s
        # Level 3 (high): 15s+
        
        # Timer to detect when distraction has ended (if no event for N seconds)
        self.distraction_timeout_sec = 3.0
        self.distraction_timer = None

        # Timer to trigger celebrate state after 50 minutes
        self.celebrate_timer = self.create_timer(3000.0, self.on_celebrate_timeout)

        self.get_logger().info('Main Manager initialized')

    def distraction_callback(self, msg: DistractionEvent):
        """
        Handle distraction event with three-level escalation.
        
        Levels:
        - Level 1 (low): 0-5s
        - Level 2 (medium): 5-15s
        - Level 3 (high): 15s+
        
        Escalates incrementally if distraction continues past thresholds.
        Resets to idle if no distraction event received for timeout period.
        """
        duration = msg.duration
        
        # Determine current distraction level based on duration
        if duration <= self.distraction_level_1_threshold:
            current_level = "low"
        elif duration <= self.distraction_level_2_threshold:
            current_level = "medium"
        else:
            current_level = "high"
        
        # Check if we need to escalate
        escalated = False
        if self.current_distraction_level is None or current_level != self.current_distraction_level:
            # New distraction or escalation detected (includes initial low level)
            escalated = True
            self.current_distraction_level = current_level
        
        # Log the event
        severity_desc = f"Level {['low', 'medium', 'high'].index(current_level) + 1} ({current_level})"
        escalation_note = " [ESCALATED]" if escalated else ""
        self.get_logger().info(
            f'Distraction Event: duration={duration:.2f}s, severity={severity_desc}{escalation_note}'
        )
        
        # Log to session tracker
        self.session_tracker.log_distraction(duration, current_level)
        
        # Reset and restart the distraction timeout timer
        if self.distraction_timer is not None:
            self.distraction_timer.cancel()
        self.distraction_timer = self.create_timer(
            self.distraction_timeout_sec,
            self.on_distraction_timeout
        )
        
        # Only forward command if escalated (avoid spamming State Manager with same level)
        if escalated:
            command_str = f"distraction_{current_level}"
            self.send_command(command_str)

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
        elif location =="left":
            command_str = "reset_position"
            self.get_logger().info(
                f'Touch Event: {location} in state {self.state_manager_state} -> reset_position'
            )
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

    def reset_distraction_level(self):
        """Reset distraction tracking to idle (called when distraction ends)."""
        if self.current_distraction_level is not None:
            self.get_logger().info('Distraction ended, reset to idle')
            self.current_distraction_level = None
            # Send a "distraction_ended" command to State Manager
            self.send_command("distraction_ended")
        
        # Cancel the timer
        if self.distraction_timer is not None:
            self.distraction_timer.cancel()
            self.distraction_timer = None

    def on_distraction_timeout(self):
        """Called when distraction timeout expires (no new event within threshold)."""
        self.reset_distraction_level()

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
        if main_manager.distraction_timer is not None:
            main_manager.distraction_timer.cancel()
        if main_manager.celebrate_timer is not None:
            main_manager.celebrate_timer.cancel()
        main_manager.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
