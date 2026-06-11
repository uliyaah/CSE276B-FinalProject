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
            if self.music_player.playing:
                self.music_player.stop_music(wait=True)
                message += "Previous music stopped"
            response.success = False
            response.message = message + f'File {request.file_name} is not found.'
        return response

    def stop_music_callback(self, request, response):
        if self.music_player.playing:
            self.music_player.stop_music(wait=True)
            response.success = True
            response.message = 'Music playback stopped.'
        else:
            response.success = False
            response.message = 'No music is being played.'
        return response

    def get_valid_file_path(self, file_name):
        package_name = 'speaker_manager'
        package_path = get_package_share_directory(package_name)
        file_path = os.path.join(package_path, 'audio', file_name)
        if os.path.isfile(file_path):
            return file_path
        else:
            return None

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

    def stop_music_callback(self, request, response):
        if self.music_player.playing:
            self.music_player.stop_music(wait=True)
            response.success = True
            response.message = 'Music playback stopped.'
        else:
            response.success = False
            response.message = 'No music is being played.'
        return response

    def get_valid_file_path(self, file_name):
        package_name = 'speaker_manager'
        package_path = get_package_share_directory(package_name)
        file_path = os.path.join(package_path, 'audio', file_name)
        if os.path.isfile(file_path):
            return file_path
        else:
            return None

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


