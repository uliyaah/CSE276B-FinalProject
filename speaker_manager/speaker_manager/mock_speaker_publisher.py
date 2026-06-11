########
# Name: mock_speaker_publisher.py
#
# Purpose: Mock Speaker Publisher for testing.
#
# Usage: First launch the service (see lab/file). Then you can run the client like this:
#        ros2 run speaker_manager service
#
# Acknowledgements: Used some code from ROS 2 Tutorials and MangDang's ROS git repo 
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#  https://github.com/mangdangroboticsclub/mini_pupper_ros/tree/ros2-dev/mini_pupper_music 
# Date: 11 June 2026
########

import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


###
# Name: Mock Speaker Publisher
#
# Purpose: Mock Speaker Publisher for testing
#
######
class MockSpeakerPublisher(Node):
    """Publish a timed sequence of speaker commands for testing."""

    def __init__(self):
        super().__init__('mock_speaker_publisher')

        self.publisher = self.create_publisher(String, 'speaker/command', 10)

        # sequence, should correspond to sound requests in client_speaker.py
        self.sequence = [
            'celebrate',
            'whine',
            'bark',
            'silent',
        ]
        self.index = 0
        self.interval = 15.0  # seconds

        self.timer = self.create_timer(self.interval, self.publish_next)
        self.get_logger().info(f'Mock speaker publisher started ({self.interval}s interval)')

    #####
    # Name: publish_next
    # Purpose: This will publish the next speaker command in the sequence.
    # Arguments: N/A
    #####
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


