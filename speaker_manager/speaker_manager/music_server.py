#!/usr/bin/env python3
#
# Copyright 2023 MangDang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Author  : Cullen SUN

########
# Name: music_server.py
#
# Purpose: Music Server for handling music playback requests from other nodes
#
# Usage: Run the service
#     ros2 run speaker_manager music_server
#
# Author: Angie Nguyen <atn046@ucsd.edu>, Prof. Riek <lriek@ucsd.edu>
#
# Acknowledgements: Used MangDang's ROS git repo as the base, with some modifications to fit our project needs
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#  https://github.com/mangdangroboticsclub/mini_pupper_ros/tree/ros2-dev/mini_pupper_music 
# Date: 11 June 2026
########

import rclpy
from rclpy.node import Node
from pupper_interfaces.srv import PlayMusic, StopMusic
#from .music_player import MusicPlayer
from speaker_manager.music_player import MusicPlayer
import os
from ament_index_python.packages import get_package_share_directory


class MusicServiceNode(Node):
    def __init__(self):
        super().__init__('mini_pupper_music_service')
        self.music_player = MusicPlayer()
        self.play_service = self.create_service(
            PlayMusic,
            'play_music',
            self.play_music_callback
        )
        self.stop_service = self.create_service(
            StopMusic,
            'stop_music',
            self.stop_music_callback
        )

    #####
    # Name: play_music_callback
    # Purpose: It will attempt to play the requested music file, stopping any currently playing music if necessary.
    # Arguments: request - the service request containing the music file name, start second, and duration
    #            response - the service response to be filled with the success status and message
    #####
    def play_music_callback(self, request, response):
        print(f"Received request to play music: {request.file_name}, start_second: {request.start_second}, duration: {request.duration}")
        file_path = self.get_valid_file_path(request.file_name)
        message = ""
        if file_path is not None:
            if self.music_player.playing:
                self.music_player.stop_music(wait=True)
                message += "Previous music stopped - "

            self.music_player.start_music(file_path,
                                          request.start_second,
                                          request.duration)
            response.success = True
            response.message = message + 'Music started playing.'
            self.get_logger().info(f"playing music at {file_path}")
        else:
            response.success = False
            response.message = f'File {request.file_name} is not found.'
        return response

    #####
    # Name: stop_music_callback
    # Purpose: It will attempt to stop any currently playing music.
    # Arguments: request - the service request (not used)
    #            response - the service response to be filled with the success status and message
    #####
    def stop_music_callback(self, request, response):
        if self.music_player.playing:
            self.music_player.stop_music(wait=True)
            response.success = True
            response.message = 'Music playback stopped.'
        else:
            response.success = False
            response.message = 'No music is being played.'
        return response

    #####
    # Name: get_valid_file_path
    # Purpose: It will return the valid file path for the requested music file if it exists.
    # Arguments: file_name - the name of the music file
    #####
    def get_valid_file_path(self, file_name):
        package_name = 'speaker_manager'
        package_path = get_package_share_directory(package_name)
        file_path = os.path.join(package_path, 'audio', file_name)
        if os.path.isfile(file_path):
            return file_path
        else:
            return None

    #####
    # Name: destroy_node
    # Purpose: This will destroy the music service node, stopping any currently playing music and cleaning up resources.
    # Arguments: N/A
    #####
    def destroy_node(self):
        self.music_player.destroy()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    music_service_node = MusicServiceNode()
    rclpy.spin(music_service_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


