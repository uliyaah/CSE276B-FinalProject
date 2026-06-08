import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockSpeakerPublisher(Node):
    """Publish a timed sequence of speaker commands for testing."""

    def __init__(self):
        super().__init__('mock_speaker_publisher')

        self.publisher = self.create_publisher(String, 'speaker/command', 10)

        self.sequence = [
            'music',
            'whine',
            'bark',
            'silent',
        ]
        self.index = 0
        self.interval = 15.0  # seconds

        self.timer = self.create_timer(self.interval, self.publish_next)
        self.get_logger().info(f'Mock speaker publisher started ({self.interval}s interval)')

    def publish_next(self):
        sound = self.sequence[self.index]

        msg = String()
        msg.data = json.dumps({'sound': sound})
        self.publisher.publish(msg)

        self.get_logger().info(f'Published speaker command: {msg.data}')

        self.index = (self.index + 1) % len(self.sequence)


def main(args=None):
    rclpy.init(args=args)
    node = MockSpeakerPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down mock speaker publisher')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

