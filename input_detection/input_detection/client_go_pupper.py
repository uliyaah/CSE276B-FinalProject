########
# Name: client_go_pupper.py
#
# Purpose: Go Pupper Client. Sample client code which will communicate with the GoPupper service by
#          passing touch input from the user as a string and touch duration, additionally updating the image to reflect move direction
#
# Usage: First launch the service (see lab/file). Then you can run the client like this:
#        ros2 run lab2task5 client
#
# Acknowledgements: Used some code from ROS 2 Tutorials and MangDang's ROS git repo 
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html#test-the-new-interfaces
#  https://github.com/mangdangroboticsclub/mini_pupper_ros/blob/ros2-dev/mini_pupper_dance/mini_pupper_dance/dance_server.py
#
# Date: 11 May 2026
########


# Import the ROS2 interface we wrote, called GoPupper. This specifies the message type.
from pupper_interfaces.srv import GoPupper

# Lets us read arguments from the command line as needed
import sys

# Packages to let us create nodes and spin them up
import rclpy
from rclpy.node import Node

# Packages for GPIO and timers
import time
import RPi.GPIO as GPIO

# Pupper libraries for using the LCD Display. Display provies basic functions,
# BehaviorState allows you to change the display's state depending on the robot
# (e.g., low battery, boot, etc). 
from MangDang.mini_pupper.display import Display, BehaviorState
import time
from resizeimage import resizeimage  # library for image resizing
from PIL import Image, ImageDraw, ImageFont # library for image manip.

###
# Name: Minimal Client Async
#
# Purpose: "The MinimalClientAsync class constructor initializes the node with the name minimal_client_async. "
#          "The constructor definition creates a client with the same type and name as the service node. 
#          The type and name must match for the client and service to be able to communicate."
#
# Prof Riek Notes: You can call this method whatever you like, this is just the modified ROS tutorial code. 
######
class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        #super().__init__('client_go_pupper')
        self.cli = self.create_client(GoPupper, 'pup_command')


        # "The while loop in the constructor checks if a service matching the type and name of the client 
        # is available once a second." 
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        # "Finally it creates a new request object.""
        self.req = GoPupper.Request()

    ###
    # Name: send_move_request
    # Purpose: send_move_request method, send request and spin until receive response or fail
    # Arguments:  self (reference the current class), move_command (the command we plan to send to the server)
    #####
    def send_move_request(self, move_command, duration):
        self.req = GoPupper.Request()
        self.req.command = move_command
        self.req.duration = duration
        print("In send_move_request, command is: %s, duration: %.3f" % (self.req.command, self.req.duration))
        self.future = self.cli.call_async(self.req)  # send the command to the server
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

# GPIO setup for touch sensors
touchPin_Front = 6
touchPin_Left  = 3
touchPin_Right = 16

# Use GPIO number but not PIN number
GPIO.setmode(GPIO.BCM)

# Set up GPIO numbers to input
GPIO.setup(touchPin_Front, GPIO.IN)
GPIO.setup(touchPin_Left,  GPIO.IN)
GPIO.setup(touchPin_Right, GPIO.IN)

#####
# Name: check_touch_input
# Purpose: This will check for touch input from the GPIO pins and return a string command to send to the server.
# Arguments: N/A
#####
def check_touch_input():
    touchValue_Front = GPIO.input(touchPin_Front)
    touchValue_Left  = GPIO.input(touchPin_Left)
    touchValue_Right = GPIO.input(touchPin_Right)
    move_string = ''
    if not touchValue_Left and not touchValue_Right:
        # not accepted, stay still if both left and right are touched
        move_string = 'stay'
    elif not touchValue_Front and not touchValue_Left:
        move_string = 'move_front_left'
    elif not touchValue_Front and not touchValue_Right:
        move_string = 'move_front_right'
    elif not touchValue_Front:
        move_string = 'move_front'
    elif not touchValue_Right:
        move_string = 'move_right'
    elif not touchValue_Left:
        move_string = 'move_left'
    else:
        move_string = 'stay'

    return move_string

MAX_WIDTH = 320   # max width of the LCD display
# Get access to the display so we can display things
disp = Display()
###
# Name: change_display
# Purpose: Take the move command and change the image on the display accordingly.
# Arguments: move_command which represents the command sent to the server
#####
def change_display(move_command):
    # set default to stay
    imgLoc = "/home/ubuntu/tmp/img/stay.png"
    if move_command == 'move_front_left' or move_command == 'move_front_right':
        imgLoc = "/home/ubuntu/tmp/img/f_leftright.png"
    elif move_command == 'move_front':
        imgLoc = "/home/ubuntu/tmp/img/dog.jpg"
    elif move_command == 'move_right' or move_command == 'move_left':
        imgLoc = "/home/ubuntu/tmp/img/leftright.png"

    imgFile = Image.open(imgLoc)

    if move_command == 'move_front_left' or move_command == 'move_right':
        imgFile = imgFile.transpose(Image.FLIP_LEFT_RIGHT)

    # Convert to RGBA if needed
    if (imgFile.format == 'PNG'):
        if (imgFile.mode != 'RGBA'):
            imgOld = imgFile.convert("RGBA")
            imgFile = Image.new('RGBA', imgOld.size, (255, 255, 255))

    # We likely also need to resize to the pupper LCD display size (320x240).
    # Note, this is sometimes a little buggy, but you can get the idea. 
    width_size = (MAX_WIDTH / float(imgFile.size[0]))
    imgFile = resizeimage.resize_width(imgFile, MAX_WIDTH)

    newFileLoc = '/home/ubuntu/tmp/animeRZ.png'   #rename as you like

    # now output it (super inefficient, but it is what it is)
    imgFile.save(newFileLoc, imgFile.format)

    # Display it on Pupper's LCD display
    disp.show_image(newFileLoc)

###
# Name: Main
# Purpose: "Within a loop, constructs a MinimalClientAsync object, checks for touch input, and sends the move command with its duration to the server while changing display image to reflect the command, checking for a response."
# Arguments: N/A
#####
def main(args=None):
    rclpy.init(args=args)
    last_time = time.time()
    duration = 0.0
    last_command = 'stay'
    while True:
        minimal_client = MinimalClientAsync()
        move_command = check_touch_input()
        if last_command != move_command:
            last_time = time.time() # reset the timer if the command changes
        current_time = time.time() 
        duration = current_time - last_time # calculate how long we've been in the current command state
        # Call send move request (which sends cmd to server)
        change_display(move_command)
        minimal_client.send_move_request(move_command, duration)
        last_command = move_command
        while rclpy.ok():
            # This spins up a client node, checks if it's done, throws an exception of there's an issue
            # (Probably a bit redundant with other code and can be simplified. But right now it works, so ¯\_(ツ)_/¯)
            rclpy.spin_once(minimal_client)
            if minimal_client.future.done():
                try:
                    response = minimal_client.future.result()

                except Exception as e:
                    minimal_client.get_logger().info(
                        'Service call failed %r' % (e,))
                else:
                    minimal_client.get_logger().info(
                    'Result of command: %s ' %
                    (response))
                break

        time.sleep(0.1)  # sleep for a bit to avoid spamming the server with requests

        # Destroy node and shut down
        minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()