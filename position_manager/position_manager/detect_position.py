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


# Creating a class for the detect_position node. Note that this class inherits from the Node class.
class detect_position(Node):
    def __init__(self):
        #Initializing a node with the name 'detect_position'
        super().__init__('detect_position')
        #Subscribing to the /oak/rgb/image_raw topic that carries data of Image type
        self.img_subscription = self.create_subscription(Image, '/oak/rgb/image_raw', self.store_img, 10)
        self.img_subscription #this is just to remove unused variable warnings

        self.cmd_subscription = self.create_subscription(String, 'movement/command', self.set_command, 10)
        #publish to topic client_position takes in 
        self.pose_publisher_ = self.create_publisher(Pose, "/body_pose", 10)
        #self.mvmt_resp_publisher_ = self.create_publisher(String, "/movement_response",10)
        self.cli = self.create_client(GoPupper, 'pup_command')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')    
    
        #CvBridge has functions that allow you to convert ROS Image type data into OpenCV images
        self.br = CvBridge()

        self.pink_lower = [160,80,10]
        self.pink_upper = [185,255,255]
        
        #DEFINE POSITION/RANGE WHERE MARKER SHOULD BE
        
        self.is_moving = False
        self.latest_command = None
        self.latest_img = None
        self.align_attempts = 0
        self.num_forward_paces = 0

    
    def store_img(self, data):
        self.latest_img = self.br.imgmsg_to_cv2(data)

    def set_command(self, msg ):
        self.latest_command = msg.data

    def retrieve_img(self):
        self.latest_img = None
        while self.latest_img is None:
            rclpy.spin_once(self, timeout_sec=0.05)
        return self.latest_img.copy()
    
    def get_pos(self, frame):
        hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_pink = np.array(self.pink_lower)
        upper_pink = np.array(self.pink_upper)
        mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)

        contours, _ = cv2.findContours(mask_pink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            print(f"did not find contours\n")
            return None

        largest  = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        if area < 200:
            print(f"contour area too small\n")         
            return None

        M  = cv2.moments(largest)
        cx = int(M['m10'] / M['m00'])
        return cx

    def send_move_command(self, move_command):
        self.req = GoPupper.Request()
        self.req.command = move_command
        print("In send_move_request, command is: %s" % self.req.command)
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

   # def send_mvmt_response(self):
    #    msg = String()
    #    msg.data = "complete"
    #    self.mvmt_resp_publisher_.publish(msg)

    def move_towards(self):
        self.face_towards()
        self.send_move_command("move_front")
        self.num_forward_paces += 1
   #     self.send_mvmt_response()

    def move_away(self):
        
        self.get_up()
        time.sleep(0.5)
        self.face_towards()
        while self.num_forward_paces != 0:
            self.send_move_command( "move_back")
            self.num_forward_paces -= 1
    #        self.send_mvmt_response()

    def check_is_aligned(self):
        frame = self.retrieve_img()
        cx = self.get_pos(frame)
        if(cx is None):
            print(f"cx was NONE in check_is_aligned\n")
            return False
        frame_cx = frame.shape[1] // 2
        return abs(cx - frame_cx) < 100
    
    def shake(self):
       # self.face_towards()
        #self.send_move_command("turn_right")
       # self.send_move_command("turn_left")
       # self.send_move_command("turn_right")
       # self.face_towards()
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
     #   self.send_mvmt_response()

    def face_towards(self):
        self.align_attempts = 0
        while(self.align_attempts < 5):
            frame = self.retrieve_img()
            cx = self.get_pos(frame)
            frame_cx = frame.shape[1] // 2
            print(f"frame_shape = {frame.shape}\n")
            print(f"frame_cx = {frame_cx}\n")
            print(f"cx = {cx}\n")
           
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


    def face_away(self):
        self.align_attempts = 0
        if(not self.check_is_aligned()):
            self.align_attempts = 0
            return
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
    
    def beg(self):
        self.move_towards()
        self.tilt()
        #time.sleep(5)
        #self.get_up()
        #time.sleep(1)
      #  self.send_mvmt_response()
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


    def tilt(self):
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

# Main function         
def main(args=None):
    # Initializing rclpy (ROS Client Library for Python)
    rclpy.init(args=args)
    
    #Create an object of the echo_camera class
    echo_obj = detect_position()
    
    while rclpy.ok():
        #cmd = input("enter approach, move_away, align, face_away, beg, shake:\n")
        rclpy.spin_once(echo_obj, timeout_sec=0.1)
        if echo_obj.latest_command == "approach":
            echo_obj.move_towards()
            echo_obj.latest_command = None
        elif echo_obj.latest_command == "move_away":
            echo_obj.move_away()
            echo_obj.latest_command = None
        elif echo_obj.latest_command == "align":
            echo_obj.face_towards()
            echo_obj.latest_command = None
        elif echo_obj.latest_command == "face_away":
            echo_obj.face_away()
            echo_obj.latest_command = None
        elif echo_obj.latest_command == "beg":
            echo_obj.beg()
            echo_obj.latest_command = None
        elif echo_obj.latest_command == "shake":
            echo_obj.shake()
            echo_obj.latest_command = None
                    
    #Destroy node when done 
    echo_obj.destroy_node()
    
    #Shutdown rclpy
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
