########
# Name: movement_manager.py
#
# Purpose: Detect position of user and execute movement relative to user's position. 
#           Code which will send requests of movement commands to service_position and
#           also send Pose messages to change body pose
#
# Usage: After conpling and sourcing the ~/ros2_ws/install/setup.bash , launch the service like this:
#         ros2 run position_manager movement_manager
#        (See client code for how to use)
#
# Author: Sierra Myers <ssmyers@ucsd.edu>, Prof. Riek <lriek@ucsd.edu>
#
# Acknowledgements: Used some code from Lab 1 and Lab 2,
# specifically color detection code and the some code for the client to go_pupper_service
#
# Date: 04 June 2026
#
#
########

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
from cv_bridge import CvBridge
import numpy as np
from pupper_interfaces.srv import GoPupper
from geometry_msgs.msg import Pose
from scipy.spatial.transform import Rotation
import time

####
# Name: Detect Position
#
# Purpose: "The detect_position class constructor initializes the node with the name detect_position 
#
####
class DetectPosition(Node):
    def __init__(self):
        #Initializing a node with the name 'detect_position'
        super().__init__('detect_position')
        #Subscribing to the /oak/rgb/image_raw topic that carries data of Image type
        self.img_subscription = self.create_subscription(Image, '/oak/rgb/image_raw', self.store_img, 10)
        self.img_subscription #this is just to remove unused variable warnings

        #subscribe to the topic state_manager publishes
        self.cmd_subscription = self.create_subscription(String, 'movement/command', self.set_command, 10)

        #create publisher for the topic that allows for changes of poses 
        self.pose_publisher_ = self.create_publisher(Pose, "/body_pose", 10)

        #create client to go_pupper service
        self.cli = self.create_client(GoPupper, 'pup_command')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')    
    
        #CvBridge has functions that allow you to convert ROS Image type data into OpenCV images
        self.br = CvBridge()

        #hsv values for pink color ranges (used to center to user)
        self.pink_lower = [160,80,10]
        self.pink_upper = [185,255,255]
        
        
        #initialize values
        self.latest_command = None
        self.latest_img = None
        self.align_attempts = 0
        self.num_forward_paces = 0

    
    ####
    # Name: Store Image
    # Purpose: Stores the data of the latest image received from the /oak/rgb/image_raw as a numpy array
    #####
    def store_img(self, data):
        self.latest_img = self.br.imgmsg_to_cv2(data)

    ####
    # Name: Set Command
    # Purpose: Stores the name of the latest command received by the state_manager
    #####
    def set_command(self, msg ):
        self.latest_command = msg.data

    ####
    # Name: Retreive Image
    # Purpose: Retreives the latest image from /oak/rgb/image_raw
    #####
    def retrieve_img(self):
        self.latest_img = None
        while self.latest_img is None:
            rclpy.spin_once(self, timeout_sec=0.05)
        return self.latest_img.copy()
    
    ####
    # Name: Get Position
    # Purpose: Retreives the center x value of the largest cluster of pink in the image (which represents center of user)
    #####
    def get_pos(self, frame):

        #create pink mask
        hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_pink = np.array(self.pink_lower)
        upper_pink = np.array(self.pink_upper)
        mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)

        #find groups of pink
        contours, _ = cv2.findContours(mask_pink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None

        #get largest group of pink
        largest  = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        #if it is too little on screen ignore
        if area < 200:        
            return None

        #find the center x value of the largest group of pink
        M  = cv2.moments(largest)
        cx = int(M['m10'] / M['m00'])
        return cx

    ####
    # Name: Send Move Command
    # Purpose: Sends a GoPupper request to Service Position
    #####
    def send_move_command(self, move_command):
        self.req = GoPupper.Request()
        self.req.command = move_command
        print("In send_move_request, command is: %s" % self.req.command)
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

    ####
    # Name: Move Towards
    # Purpose: Functionality to have robot align to user and move forward
    #####
    def move_towards(self):
        self.face_towards()
        self.send_move_command("move_front")
        self.num_forward_paces += 1

    ####
    # Name: Move Away
    # Purpose: Functionality to have robot align to user and move backwards the 
    #          cumalative amount is has gone forward since last being called
    #          (resets the position)
    #####
    def move_away(self):
        self.get_up()
        time.sleep(0.5)
        self.face_towards()
        while self.num_forward_paces != 0:
            self.send_move_command( "move_back")
            self.num_forward_paces -= 1

    ####
    # Name: Check is Aligned
    # Purpose: Helper function that returns true if robot is aligned to user 
    #####
    def check_is_aligned(self):

        frame = self.retrieve_img()
        cx = self.get_pos(frame)

        if(cx is None):
            return False
        
        frame_cx = frame.shape[1] // 2

        return abs(cx - frame_cx) < 100 #return true if center is within threshold
    
    ####
    # Name: Shake
    # Purpose: Functionality to have robot shake side to side
    #          (used when robot is 'barking')
    #####
    def shake(self):
        self.side_tilt(8)
        time.sleep(0.75)
        self.side_tilt(-8)
        time.sleep(0.75)
        self.side_tilt(8)
        time.sleep(0.75)
        self.side_tilt(-8)
        time.sleep(0.75)
        self.get_up()
        time.sleep(1)

    ####
    # Name: Face Towards
    # Purpose: Helper function to have robot face towards user
    #####
    def face_towards(self):
        self.align_attempts = 0
        #set max attempts of alignment to 5 to prevent oscillation / protect flow of robot behavior
        while(self.align_attempts < 5): 
            frame = self.retrieve_img()
            cx = self.get_pos(frame)
            frame_cx = frame.shape[1] // 2
           
            if(cx is None):
                self.send_move_command("turn_left")
                self.align_attempts += 1
                continue
            if(abs(cx - frame_cx) < 75):
                self.align_attempts = 0
                return
            elif(cx - frame_cx > 0):
                self.send_move_command("turn_right")
            else:
                self.send_move_command("turn_left")
            self.align_attempts += 1

    ####
    # Name: Face Away
    # Purpose: Helper function to have robot face away from user
    #          (note: we decided to not use this functionality in final robot design)
    #####
    def face_away(self):
        self.align_attempts = 0
        if(not self.check_is_aligned()):
            self.align_attempts = 0
            return
        #set max attempts of alignment to 3 to prevent oscillation / protect flow of robot behavior
        while(self.align_attempts < 3):
            frame = self.retrieve_img()
            cx = self.get_pos(frame)
            frame_cx = frame.shape[1] // 2
            if(cx is None or abs(cx - frame_cx) > 75):
                self.align_attempts = 0
                return
            else:
                self.send_move_command("turn_right")
            self.align_attempts += 1

    ####
    # Name: Beg
    # Purpose: Functionality to have robot align itself to user,
    #          go towards the user, and look up at the user
    #####   
    def beg(self):
        self.move_towards()
        self.tilt_up()

    ####
    # Name: Side Tilt
    # Purpose: Helper function to have robot tilt sideways by certain at specified certain angle
    #####
    def side_tilt(self, deg):
        roll = deg
        pitch = 0
        yaw = 0
        rotation = Rotation.from_euler('xyz', [roll, pitch, yaw], degrees=True)
        q = rotation.as_quat()

        msg = Pose()
        msg.position.x = 0.0
        msg.position.y = 0.0
        msg.position.z = 0.0

        msg.orientation.x = q[0]
        msg.orientation.y = q[1]
        msg.orientation.z = q[2]
        msg.orientation.w = q[3]

        self.pose_publisher_.publish(msg)

    ####
    # Name: Tilt Up
    # Purpose: Helper function to have robot look up at user
    #####
    def tilt_up(self):
        roll = 0
        pitch = -12
        yaw = 0
        rotation = Rotation.from_euler('xyz', [roll, pitch, yaw], degrees=True)
        q = rotation.as_quat()

        msg = Pose()
        msg.position.x = 0.0
        msg.position.y = 0.0
        msg.position.z = 0.0

        msg.orientation.x = q[0]
        msg.orientation.y = q[1]
        msg.orientation.z = q[2]
        msg.orientation.w = q[3]

        self.pose_publisher_.publish(msg)

    ####
    # Name: Get Up
    # Purpose: Helper function to have robot re-orient itself after tilting upwards to user
    #####
    def get_up(self):
        msg = Pose()
        msg.position.x = 0.0
        msg.position.y = 0.0
        msg.position.z = 0.0

        msg.orientation.x = 0.0
        msg.orientation.y = 0.0
        msg.orientation.z = 0.0
        msg.orientation.w = 1.0

        self.pose_publisher_.publish(msg)

####
# Name: Main
# Purpose: Main functoin to set up our node
#####      
def main(args=None):
    # Initializing rclpy (ROS Client Library for Python)
    rclpy.init(args=args)
    
    #Create an object of the detect_position class
    detect_obj = DetectPosition()
    
    #Loop and get latest command from state_manager
    while rclpy.ok():
        rclpy.spin_once(detect_obj, timeout_sec=0.1)
        if detect_obj.latest_command == "approach":
            detect_obj.move_towards()
            detect_obj.latest_command = None
        elif detect_obj.latest_command == "move_away":
            detect_obj.move_away()
            detect_obj.latest_command = None
        elif detect_obj.latest_command == "align": #not used by state_manager
            detect_obj.face_towards()
            detect_obj.latest_command = None
        elif detect_obj.latest_command == "face_away": #not used by state_manger
            detect_obj.face_away()
            detect_obj.latest_command = None
        elif detect_obj.latest_command == "beg":
            detect_obj.beg()
            detect_obj.latest_command = None
        elif detect_obj.latest_command == "shake":
            detect_obj.shake()
            detect_obj.latest_command = None
                    
    #Destroy node when done 
    detect_obj.destroy_node()
    
    #Shutdown rclpy
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
