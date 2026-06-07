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
#     "face": "idle|sleep|offended|puppy_dog_eyes|puppy_dog_eyes2",
#     "interval": 0.5  (time in seconds between image switches, default: 0.5)
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
from PIL import Image, ImageDraw, ImageFont  # library for image manipulation


# Display configuration
MAX_WIDTH = 320  # max width of the LCD display
DISPLAY_HEIGHT = 240  # height of the LCD display


class DisplayManager(Node):
    """
    Display Manager node that updates the Pupper's screen display.
    
    Receives display commands from State Manager via display/command topic.
    Updates the display hardware based on requested face expressions.
    Supports cycling through multiple images per reaction at configurable intervals.
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

        # Animation state tracking
        self.animation_timer = None
        self.current_face = None
        self.current_image_index = 0
        self.current_images = []
        self.animation_interval = 0.5  # Default interval in seconds

        # Subscribe to display commands from State Manager
        self.display_sub = self.create_subscription(
            String,
            'display/command',
            self.display_callback,
            10
        )
        
        # Initialize display to idle
        self.set_display('idle', 0.5)

        self.get_logger().info('Display Manager initialized and listening on display/command')

    def display_callback(self, msg: String):
        """
        Callback for display command messages.
        
        Args:
            msg: String message containing JSON display command
                 Format: {"face": "idle", "interval": 0.5}
                 interval (optional): Time in seconds between image switches (default: 0.5)
        """
        try:
            # Parse JSON display command
            command = json.loads(msg.data)
            face = command.get('face', 'idle')
            interval = command.get('interval', 0.5)
            
            self.get_logger().info(f'Display command received: {face} with interval {interval}s')
            
            # Route to appropriate display handler
            self.set_display(face, interval)
            
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Failed to parse display command: {e}')
        except Exception as e:
            self.get_logger().error(f'Error processing display command: {e}')

    def set_display(self, face: str, interval: float = 0.5):
        """
        Set the display to show the requested face expression and cycle through images.
        
        Args:
            face: String identifier for the face expression (idle, sleep, offended, etc.)
            interval: Time in seconds between image switches
        """
        # Cancel any existing animation timer
        if self.animation_timer is not None:
            self.destroy_timer(self.animation_timer)
            self.animation_timer = None
        
        # Get all images for the requested face
        face_dir = self.images_dir / face
        
        if not face_dir.exists():
            self.get_logger().warn(f'Face directory not found: {face_dir}')
            return
        
        # Get all PNG images in the directory, sorted
        self.current_images = sorted([
            f for f in face_dir.iterdir()
            if f.suffix.lower() in ['.png', '.jpg', '.jpeg']
        ])
        
        if not self.current_images:
            self.get_logger().warn(f'No images found in {face_dir}')
            return
        
        self.current_face = face
        self.current_image_index = 0
        self.animation_interval = interval
        
        self.get_logger().info(f'Starting animation for {face} with {len(self.current_images)} images at {interval}s interval')
        
        # Display the first image
        self.display_next_image()
        
        # Create timer for animation cycling
        self.animation_timer = self.create_timer(interval, self.display_next_image)
    
    def display_next_image(self):
        """
        Display the next image in the animation sequence.
        Cycles back to the first image when reaching the end.
        """
        if not self.current_images:
            return
        
        # Get the current image
        image_path = self.current_images[self.current_image_index]
        
        # Show the image
        self.show_image_on_display(str(image_path))
        
        # Move to next image
        self.current_image_index = (self.current_image_index + 1) % len(self.current_images)

    def show_image_on_display(self, image_path: str):
        """
        Load, resize, and display an image on the Pupper's LCD display.
        
        Args:
            image_path: Full path to image file
        """
        if not self.disp:
            self.get_logger().warn('Display not initialized, skipping image display')
            return

        try:
            # Convert to Path object if needed
            img_path = Path(image_path)
            
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
            # Use PIL's resize which can upscale if needed
            img_file = img_file.resize((MAX_WIDTH, DISPLAY_HEIGHT), Image.Resampling.LANCZOS)
            
            # Create temporary resized image
            resized_filename = img_path.stem + '_resized.png'
            resized_path = self.images_dir / resized_filename
            img_file.save(str(resized_path), img_file.format)
            
            # Display on Pupper's LCD
            self.disp.show_image(str(resized_path))
            self.get_logger().info(f'Displayed image: {img_path.name}')
            
        except Exception as e:
            self.get_logger().error(f'Error displaying image {image_path}: {e}')


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
