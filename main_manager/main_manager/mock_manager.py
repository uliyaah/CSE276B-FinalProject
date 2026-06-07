import json
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pupper_interfaces.msg import DistractionEvent, TouchEvent


class MainManagerTester(Node):
    """Test Main Manager by publishing distraction/touch events and observing state changes."""

    def __init__(self):
        super().__init__('main_manager_tester')

        # Publishers for test events
        self.distraction_pub = self.create_publisher(DistractionEvent, 'distraction_event', 10)
        self.touch_pub = self.create_publisher(TouchEvent, 'touch_event', 10)

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

    def run_test_step(self):
        """Execute test steps sequentially."""
        if self.test_step == 0:
            self.get_logger().info('=== TEST 1: Low distraction (2 sec) ===')
            self.publish_distraction(duration_sec=2.0)
            self.test_step += 1

        elif self.test_step == 5:
            self.get_logger().info('=== TEST 2: Medium distraction (10 sec) ===')
            self.publish_distraction(duration_sec=10.0)
            self.test_step += 1

        elif self.test_step == 15:
            self.get_logger().info('=== TEST 3: High distraction (20 sec) ===')
            self.publish_distraction(duration_sec=20.0)
            self.test_step += 1

        elif self.test_step == 35:
            self.get_logger().info('=== TEST 4: Touch event (pause) ===')
            self.publish_touch()
            self.test_step += 1

        elif self.test_step == 40:
            self.get_logger().info('=== TEST 5: Touch again (resume) ===')
            self.publish_touch()
            self.test_step += 1

        elif self.test_step == 45:
            self.get_logger().info('All tests complete. Summary:')
	    self.get_logger().info('=== State Transitions ===')
            for result in self.test_results:
                self.get_logger().info(f'  {result}')
            self.get_logger().info('=== Display Commands ===')
            for idx, cmd in enumerate(self.display_commands):
                self.get_logger().info(f'  {idx+1}. Face: {cmd["face"]}, Interval: {cmd["interval"]}s')

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
