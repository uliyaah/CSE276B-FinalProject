import rclpy
from rclpy.node import Node

from pupper_interfaces.srv import CameraPupper
from pupper_interfaces.msg import DistractionEvent

class CameraDurationService(Node):
    def __init__(self):
        super().__init__('camera_duration_service')

        self.srv = self.create_service(CameraPupper, 'camera_command', self.camera_callback)
        self.distraction_publisher_ = self.create_publisher(DistractionEvent, 'distraction_event', 10)
        self.get_logger().info('Distraction event publisher service started')


    def camera_callback(self, request, response):
        duration = float(request.duration)

        self.get_logger().info('Color present for %.3f s' % duration)
            
        # Publish distraction event
        distraction_event = DistractionEvent()
        distraction_event.duration = duration
        self.distraction_publisher_.publish(distraction_event)
        self.get_logger().info('Published distraction event with duration=%.3f s' % duration)

        response.executed = True
        return response


def main():
    rclpy.init()
    node = CameraDurationService()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
