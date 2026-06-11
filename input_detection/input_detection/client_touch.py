########
# Name: client_touch.py
#
# Purpose: Touch Pupper Client. Sample client code which will communicate with the TouchPupper service by
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


# Import the ROS2 interface we wrote, called TouchEvent. This specifies the message type.
from pupper_interfaces.msg import TouchEvent

# Packages to let us create nodes and spin them up
import rclpy
from rclpy.node import Node

# Packages for GPIO and timers
import time
import RPi.GPIO as GPIO


###
# Name: Touch Event Publisher
#
# Purpose: Reads GPIO touch input and publishes TouchEvent messages
#
######
class TouchEventPublisher(Node):

    def __init__(self):
        super().__init__('touch_event_publisher')
        self.touch_event_publisher_ = self.create_publisher(TouchEvent, 'touch_event', 10)
        self.get_logger().info('Touch event publisher service started')


    def publish_touch(self, location):
        touch_event = TouchEvent()
        touch_event.location = location
        self.touch_event_publisher_.publish(touch_event)
        self.get_logger().info('Published touch event: location="%s"' % location)

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

###
# Name: Main
# Purpose: Reads GPIO touch input, publishes TouchEvent messages, and updates display
# Arguments: N/A
#####
def main(args=None):
    rclpy.init(args=args)
    publisher = TouchEventPublisher()
    last_command = 'stay'
    
    while rclpy.ok():
        move_command = check_touch_input()
        
        if last_command != move_command:
            # Map command to touch location
            if move_command in ['move_front', 'move_front_left', 'move_front_right']:
                publisher.publish_touch('front')
            elif move_command == 'move_left':
                publisher.publish_touch('left')
            elif move_command == 'move_right':
                publisher.publish_touch('right')
            
            last_command = move_command
        
        time.sleep(0.1)
    
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
