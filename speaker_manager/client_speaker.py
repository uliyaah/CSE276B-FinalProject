import json
import os
import shlex
import shutil
import signal
import subprocess
from pathlib import Path

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sounddevice as sd

class SpeakerClient(Node):
	def __init__(self):
		super().__init__('speaker_client')

		self.subscription = self.create_subscription(
			String,
			'speaker/command',
			self.command_callback,
			10,
        )

		print('Speaker client listening on topic: speaker/command')

	def command_callback(self, msg: String):
		sound = self._extract_sound_command(msg.data)
		if sound is None:
			print(f'Ignoring malformed speaker command: {msg.data}')
			return

		if sound == self.active_sound and sound == 'music':
			return

		self._apply_sound(sound)

	def _apply_sound(self, sound: str):
		print("Setting speaker to: %s" % sound)
		if sound == 'silent':
			return
		elif sound == 'music':
			sd.play('./sounds/small-dog-barks-aggressively-gfx-sounds-2-2-00-00.mp3')
		elif sound == 'bark':
			sd.play('./sounds/small-dog-barks-aggressively-gfx-sounds-2-2-00-00.mp3')
		elif sound == 'whine':
			sd.play('./sounds/small-dog-whines-aggressively-gfx-sounds-2-2-00-00.mp3')
		else:
			print(f'Unknown sound command: {sound}')

def main(args=None):
	# Initializing rclpy (ROS Client Library for Python)
	rclpy.init(args=args)
	
	#Create an object of the SpeakerClient class
	node = SpeakerClient()
	
	#Keep going till termination
	rclpy.spin(node)
	
	#Destroy node when done 
	node.destroy_node()
	
	#Shutdown rclpy
	rclpy.shutdown()


if __name__ == '__main__':
	main()
