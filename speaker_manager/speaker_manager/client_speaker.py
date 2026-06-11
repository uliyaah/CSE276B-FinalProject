import json
import os
import shlex
import shutil
import signal
import subprocess
from pathlib import Path

import argparse

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sounddevice as sd
import soundfile as sf

from pupper_interfaces.srv import PlayMusic, StopMusic

class SpeakerClient(Node):
	def __init__(self):
		super().__init__('speaker_client')
		
		self.subscription = self.create_subscription(
			String,
			'speaker/command',
			self.command_callback,
			10,
        )

		# also connect to MusicPlayer to play music when needed
		self.playMusicClient = self.create_client(PlayMusic, 'play_music')
		while not self.playMusicClient.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('play music service not available, waiting again...')

		self.stopMusicClient = self.create_client(StopMusic, 'stop_music')
		while not self.stopMusicClient.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('stop music service not available, waiting again...')

		self.req_play = PlayMusic.Request()
		self.req_stop = StopMusic.Request()
		self.pending_futures = set()

		print('Speaker client listening on topic: speaker/command')
		print('Play Music service client ready to call: play_music')
		print('Stop Music service client ready to call: stop_music')

	def command_callback(self, msg: String):
		sound = json.loads(msg.data)['sound']

		self.apply_sound(sound)

	def apply_sound(self, sound: str):
		print("Setting speaker to: %s" % sound)
		soundFileStr = None
		num_loops = 1
		if sound == 'silent':
			soundFileStr = 'SILENCE'
		elif sound == 'bark':
			soundFileStr = 'bark.wav'
			num_loops = 2
		elif sound == 'whine':
			soundFileStr = 'whine.wav'
			num_loops = float('inf')  # Loop indefinitely for whine
		elif sound == "celebrate":
			soundFileStr = 'celebrate.wav'
		else:
			print(f'Unknown sound command: {sound}')
			return

		self.req_play = PlayMusic.Request()
		self.req_play.file_name = soundFileStr
		self.req_play.num_loops = float(num_loops)
		print(f"Requesting to play music file: {self.req_play.file_name}")
		future = self.playMusicClient.call_async(self.req_play)
		self.pending_futures.add(future)
		future.add_done_callback(self._handle_play_music_response)
		return future

	def _handle_play_music_response(self, future):
		self.pending_futures.discard(future)
		try:
			response = future.result()
			print(f"Play music service response: {response.message}")
		except Exception as exc:
			self.get_logger().error(f'Play music service call failed: {exc}')

	def _handle_stop_music_response(self, future):
		self.pending_futures.discard(future)
		try:
			response = future.result()
			print(f"Stop music service response: {response.message}")
		except Exception as exc:
			self.get_logger().error(f'Stop music service call failed: {exc}')

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


