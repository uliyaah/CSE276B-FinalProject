import rclpy
from rclpy.node import Node

from pupper_interfaces.srv import CameraPupper

class CameraDurationService(Node):
    def __init__(self):
        super().__init__('camera_duration_service')

        self.srv = self.create_service(CameraPupper, 'camera_command', self.camera_callback)

    def camera_callback(self, request, response):
        duration = max(0.0, float(request.duration))

        if duration > 0.0:
            self.get_logger().info('Color present for %.3f s' % duration)
        else:
            self.get_logger().info('Received non-positive duration.')

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
