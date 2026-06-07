########
# Name: client_go_pupper.py
#
# Purpose: Go Pupper Client. Sample client code which will communicate with the GoPupper service by
#          passing touch input from the user as a string, additionally updating the image to reflect move direction
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
from std_msgs.msg import String
import time


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

        self.subscription = self.create_subscription(String, 'pupper/cmd', self.command_callback,10)
        # "The while loop in the constructor checks if a service matching the type and name of the client 
        # is available once a second." 
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        # "Finally it creates a new request object.""
        self.req = GoPupper.Request()

        self.latest_msg = None

    def command_callback(self, msg):
        self.latest_msg = msg.data 

    ###
    # Name: send_move_request
    # Purpose: send_move_request method, send request and spin until receive response or fail
    # Arguments:  self (reference the current class), move_command (the command we plan to send to the server)
    #####
    def send_move_request(self, move_command):
        self.req = GoPupper.Request()
        self.req.command = move_command
        print("In send_move_request, command is: %s" % self.req.command)
        self.future = self.cli.call_async(self.req)  # send the command to the server
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()



###
# Name: Main
# Purpose: "Within a loop, constructs a MinimalClientAsync object, checks for touch input, and sends the move command to the server while changing display image to reflect the command, checking for a response."
# Arguments: N/A
#####
def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    while True:


        ### CHANGE THIS LOGIC
        while rclpy.ok() and minimal_client.latest_msg is None:
            rclpy.spin_once(minimal_client, timeout_sec=0.1)

        minimal_client.send_move_request(minimal_client.latest_msg)
        minimal_client.latest_msg = None
    
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


