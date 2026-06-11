import json
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pupper_interfaces.msg import DistractionEvent, TouchEvent, Command
from pupper_interfaces.srv import StateManagerCommand


class MainManagerTester(Node):
    """Test Main Manager by publishing distraction/touch events and observing state changes."""

    def __init__(self):
        super().__init__('main_manager_tester')

        # Publishers for test events
        self.distraction_pub = self.create_publisher(DistractionEvent, 'distraction_event', 10)
        self.touch_pub = self.create_publisher(TouchEvent, 'touch_event', 10)

        # Service client to send commands directly to State Manager
        self.state_manager_cli = self.create_client(
            StateManagerCommand,
            'state_manager_command'
        )

        # Subscriber to observe state changes
        self.state_sub = self.create_subscription(
            String,
            'state_manager/state',
            self.on_state_change,
            10
        )

        # Subscriber to observe display commands
        self.display_sub = self.create_subscription(
            String,
            'display/command',
            self.on_display_command,
            10
        )

        # Test scenario counter
        self.test_step = 0
        self.test_results = []
        self.display_commands = []  # Track display commands during test

        # Start test sequence
        self.timer = self.create_timer(1.0, self.run_test_step)
        self.get_logger().info('Main Manager Tester started')
        self.get_logger().info('Listening on: distraction_event, touch_event, state_manager/state, display/command')

    def run_test_step(self):
        """Execute test steps sequentially."""
        if self.test_step == 0:
            self.get_logger().info('=== TEST 0: Activate pupper (touch front) ===')
            self.publish_touch()

        elif self.test_step == 2:
            self.get_logger().info('=== TEST 1: Single 30-second distraction (timeline-based escalation) ===')
            self.get_logger().info('  - At 5s: should escalate to INTERVENTION_2')
            self.get_logger().info('  - At 15s: should escalate to INTERVENTION_3')
            self.get_logger().info('  - At 30s: should end and return to SENTRY')
            self.publish_distraction(duration_sec=30.0)

        elif self.test_step == 37:
            self.get_logger().info('=== TEST 2: Touch event (pause) - should be back in SENTRY by now ===')
            self.publish_touch()

        elif self.test_step == 42:
            self.get_logger().info('=== TEST 3: Touch again (resume to previous state) ===')
            self.publish_touch()

        elif self.test_step == 52:
            self.get_logger().info('=== TEST 4: Trigger celebrate state ===')
            self.send_state_command("celebrate")
            self.test_step += 1

        elif self.test_step == 57:
            self.get_logger().info('All tests complete. Summary:')
            self.get_logger().info('=== Expected State Sequence ===')
            self.get_logger().info('  1. IDLE → SENTRY (activation)')
            self.get_logger().info('  2. SENTRY → INTERVENTION_1 (distraction_low at 0s)')
            self.get_logger().info('  3. INTERVENTION_1 → INTERVENTION_2 (distraction_medium at 5s)')
            self.get_logger().info('  4. INTERVENTION_2 → INTERVENTION_3 (distraction_high at 15s)')
            self.get_logger().info('  5. INTERVENTION_3 → SENTRY (distraction_ended at 30s)')
            self.get_logger().info('  6. SENTRY → PAUSED (pause touch at 37s)')
            self.get_logger().info('  7. PAUSED → SENTRY (resume touch at 42s)')
            self.get_logger().info('  8. SENTRY → CELEBRATE (celebrate command at 52s)')
            self.get_logger().info('=== Actual State Transitions ===')
            for result in self.test_results:
                self.get_logger().info(f'  {result}')
            self.get_logger().info('=== Display Commands ===')
            if self.display_commands:
                for idx, cmd in enumerate(self.display_commands):
                    self.get_logger().info(f'  {idx+1}. Face: {cmd["face"]}, Interval: {cmd["interval"]}s')
            else:
                self.get_logger().warn('  NO DISPLAY COMMANDS RECEIVED!')
                self.get_logger().warn('  Check: Is state_manager running? Is main_manager calling it?')
            self.timer.cancel()

        self.test_step += 1

    def publish_distraction(self, duration_sec: float):
        """Publish a distraction event."""
        msg = DistractionEvent()
        msg.duration = duration_sec
        self.distraction_pub.publish(msg)
        self.get_logger().info(f'Published distraction: {duration_sec}s')

    def publish_touch(self):
        """Publish a touch event."""
        msg = TouchEvent()
        msg.location = "front"
        # msg.timestamp = int(time.time() * 1000)
        self.touch_pub.publish(msg)
        self.get_logger().info('Published touch event')
    def send_state_command(self, command_str: str):
        """Send a command directly to State Manager service."""
        request = StateManagerCommand.Request()
        request.command = Command()
        request.command.command = command_str
        
        future = self.state_manager_cli.call_async(request)
        future.add_done_callback(self.on_state_command_response)
        self.get_logger().info(f'✓ Sent command: {command_str}')

    def on_state_command_response(self, future):
        """Handle response from state manager service."""
        try:
            response = future.result()
            if response.success:
                self.get_logger().debug('State Manager accepted command')
            else:
                self.get_logger().warn('State Manager rejected command')
        except Exception as e:
            self.get_logger().error(f'State Manager call failed: {e}')

    def on_state_change(self, msg: String):
        """Log state changes from State Manager."""
        state = msg.data
        self.get_logger().info(f'>>> STATE CHANGED: {state}')
        self.test_results.append(f'State transition to {state}')

    def on_display_command(self, msg: String):
        """Log display commands from State Manager."""
        try:
            command = json.loads(msg.data)
            face = command.get('face', 'unknown')
            interval = command.get('interval', 0.5)
            self.get_logger().info(f'    [Display] Face: {face}, Interval: {interval}s')
            self.display_commands.append({'face': face, 'interval': interval})
        except json.JSONDecodeError:
            self.get_logger().warn(f'Failed to parse display command: {msg.data}')
        except Exception as e:
            self.get_logger().error(f'Error in on_display_command: {e}')


def main(args=None):
    rclpy.init(args=args)
    tester = MainManagerTester()

    try:
        rclpy.spin(tester)
    except KeyboardInterrupt:
        tester.get_logger().info('Shutting down Main Manager Tester')
    finally:
        tester.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
