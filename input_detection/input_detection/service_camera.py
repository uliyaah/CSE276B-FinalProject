########
# Name: service_camera.py
#
# Purpose: Camera Pupper Service. Sample service code which will communicate with the CameraPupper client by
#          handling camera commands and publishing image data
#
# Usage: First launch the service (see lab/file). Then you can run the client like this:
#        ros2 run input_detection service_camera
#
# Acknowledgements: Used some code from ROS 2 Tutorials and MangDang's ROS git repo 
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#
# Date: 11 June 2026
########

import rclpy
from rclpy.node import Node

from pupper_interfaces.srv import CameraPupper
from pupper_interfaces.msg import DistractionEvent

###
# Name: Camera Duration Service
#
# Purpose: Handles camera commands and publishes image data
#
######
class CameraDurationService(Node):
    def __init__(self):
        super().__init__('camera_duration_service')

        self.srv = self.create_service(CameraPupper, 'camera_command', self.camera_callback)
        self.distraction_publisher_ = self.create_publisher(DistractionEvent, 'distraction_event', 10)
        self.get_logger().info('Distraction event publisher service started')

    #####
    # Name: camera_callback
    # Purpose: This will handle camera commands from the client and publish distraction events.
    # Arguments: request - the service request containing the camera command
    #            response - the service response to be sent back to the client
    #####
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
