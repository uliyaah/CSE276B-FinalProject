import time

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image

from pupper_interfaces.srv import CameraPupper


class CameraDurationClient(Node):
    def __init__(self):
        super().__init__('camera_duration_client')

        self.cli = self.create_client(CameraPupper, 'camera_command')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('camera service not available, waiting again...')

        self.br = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/oak/rgb/image_raw',
            self.check_color_in_frame,
            10,
        )

        self.last_frame = None # Store the last frame for potential debugging or visualization purposes.
        self.color_started_at = None # Timestamp for when the target color was first detected.
        self.color_is_visible = False # Flag to track whether the target color is currently visible in the camera feed.

        # Environment constraint -- assume the phone will be bright yellow
        self.yellow_lower = np.array([25, 100, 55])
        self.yellow_upper = np.array([35, 255, 255])
        self.visibility_threshold = 0.03 # Percentage of the frame that must be the target color to consider it "visible"

        # Send duration updates at this interval (in seconds) when the color is visible
        self.timer = self.create_timer(0.2, self.send_duration_update)

    def check_color_in_frame(self, data):
        frame = self.br.imgmsg_to_cv2(data)
        self.last_frame = frame

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_yellow = cv2.inRange(hsv, self.yellow_lower, self.yellow_upper)

        color_visible = np.mean(mask_yellow) > self.visibility_threshold

        # Check if color was newly detected, ongoing, or just disappeared to manage timing and logging appropriately.
        if color_visible and not self.color_is_visible:
            self.color_started_at = time.time()
            self.get_logger().info('Target color detected.')
        elif not color_visible and self.color_is_visible:
            self.get_logger().info('Target color disappeared.')
        self.color_is_visible = color_visible


    def send_duration_update(self):
        # only send updates if the color is currently visible and we have a valid start time to calculate duration from
        duration = -1.0
        if not self.color_is_visible:
            if self.color_started_at != None:
                self.get_logger().info('Color is no longer visible. Resetting duration timer.')
                self.color_started_at = None # Reset start time if color is not visible to avoid stale duration calculations
                duration = -1.0
        else:
            duration = float(time.time() - self.color_started_at)

        req = CameraPupper.Request()
        req.duration = duration

        future = self.cli.call_async(req)
        future.add_done_callback(self.on_response)

    def on_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Sent color duration update. executed={response.executed}')
        except Exception as exc:
            self.get_logger().error(f'Camera service call failed: {exc!r}')


def main(args=None):
    # Initializing rclpy (ROS Client Library for Python)
	rclpy.init(args=args)
	
	#Create an object of the CameraDurationClient class
	node = CameraDurationClient()
	
	#Keep going till termination
	rclpy.spin(node)
	
	#Destroy node when done 
	node.destroy_node()
	
	#Shutdown rclpy
	rclpy.shutdown()


if __name__ == '__main__':
    main()
