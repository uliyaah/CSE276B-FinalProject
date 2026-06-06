########
# Name: display_manager.py
#
# Purpose: Display Manager node - receives display commands from State Manager
#          and updates the pupper's screen display.
#
# Subscribes to: display/command (String messages with JSON display commands)
# Publishes to: (none - directly updates display hardware)
#
# Display commands format:
# {
#     "face": "idle|sleep|offended|puppy_dog_eyes|puppy_dog_eyes2"
# }
#
# Date: 05 June 2026
########

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
from pathlib import Path

# Pupper libraries for using the LCD Display
from MangDang.mini_pupper.display import Display, BehaviorState
import time
from resizeimage import resizeimage  # library for image resizing
from PIL import Image, ImageDraw, ImageFont  # library for image manipulation


# Display configuration
MAX_WIDTH = 320  # max width of the LCD display
DISPLAY_HEIGHT = 240  # height of the LCD display


class DisplayManager(Node):
    """
    Display Manager node that updates the Pupper's screen display.
    
    Receives display commands from State Manager via display/command topic.
    Updates the display hardware based on requested face expressions.
    """

    def __init__(self):
        super().__init__('display_manager')

        # Initialize the Pupper display
        try:
            self.disp = Display()
            self.get_logger().info('Pupper display initialized successfully')
        except Exception as e:
            self.get_logger().error(f'Failed to initialize display: {e}')
            self.disp = None

        # Get the images directory
        self.images_dir = Path(__file__).parent / 'images'
        self.images_dir.mkdir(exist_ok=True)

        # Subscribe to display commands from State Manager
        self.display_sub = self.create_subscription(
            String,
            'display/command',
            self.display_callback,
            10
        )

        self.get_logger().info('Display Manager initialized and listening on display/command')

    def display_callback(self, msg: String):
        """
        Callback for display command messages.
        
        Args:
            msg: String message containing JSON display command
        """
        try:
            # Parse JSON display command
            command = json.loads(msg.data)
            face = command.get('face', 'idle')
            
            self.get_logger().info(f'Display command received: {face}')
            
            # Route to appropriate display handler
            self.set_display(face)
            
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Failed to parse display command: {e}')
        except Exception as e:
            self.get_logger().error(f'Error processing display command: {e}')

    def set_display(self, face: str):
        """
        Set the display to show the requested face expression.
        
        Args:
            face: String identifier for the face expression
                  (idle, sleep, offended, puppy_dog_eyes, neutral)
        """
        # Map face names to image filenames
        face_to_image = {
            'idle': 'idle.png',
            'sleep': 'sleep.png',
            'offended': 'offended.png',
            'puppy_dog_eyes': 'puppy_dog_eyes.png',
            'puppy_dog_eyes2': 'puppy_dog_eyes2.png',
        }
        
        #TODO: Upload reactions to images folder
        
        image_file = face_to_image.get(face)
        if image_file:
            self.get_logger().info(f'Setting display to {face}')
            self.show_image_on_display(image_file)
        else:
            self.get_logger().warn(f'Unknown face expression: {face}')

    def show_image_on_display(self, image_filename: str):
        """
        Load, resize, and display an image on the Pupper's LCD display.
        
        Args:
            image_filename: Path to image file (relative to images/ directory)
        """
        if not self.disp:
            self.get_logger().warn('Display not initialized, skipping image display')
            return

        try:
            # Construct full image path
            img_path = self.images_dir / image_filename
            
            if not img_path.exists():
                self.get_logger().warn(f'Image file not found: {img_path}')
                return
            
            # Open the image
            img_file = Image.open(str(img_path))
            
            # Convert to RGBA if needed (for PNG files)
            if img_file.format == 'PNG':
                if img_file.mode != 'RGBA':
                    img_old = img_file.convert("RGBA")
                    img_file = Image.new('RGBA', img_old.size, (255, 255, 255))
            
            # Resize to fit display (320x240)
            img_file = resizeimage.resize_width(img_file, MAX_WIDTH)
            
            # Create temporary resized image
            resized_filename = image_filename.rsplit('.', 1)[0] + '_resized.png'
            resized_path = self.images_dir / resized_filename
            img_file.save(str(resized_path), img_file.format)
            
            # Display on Pupper's LCD
            self.disp.show_image(str(resized_path))
            self.get_logger().info(f'Displayed image: {image_filename}')
            
        except Exception as e:
            self.get_logger().error(f'Error displaying image {image_filename}: {e}')


def main(args=None):
    """Main entry point for Display Manager node."""
    rclpy.init(args=args)
    node = DisplayManager()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
