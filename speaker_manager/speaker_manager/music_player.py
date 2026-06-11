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
# Name: music_player.py
#
# Purpose: Music Player for handling audio playback
#
# Acknowledgements: Used MangDang's ROS git repo as the base, with some modifications to fit our project needs
#  https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#  https://github.com/mangdangroboticsclub/mini_pupper_ros/tree/ros2-dev/mini_pupper_music 
# Date: 11 June 2026
########

import threading
import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks
import sounddevice

###
# Name: Music Player
#
# Purpose: Handles the actual audio playback for the speaker manager
#
######
class MusicPlayer:
    def __init__(self):
        # sounddevice is not used in any logics, just print something here
        # See: https://stackoverflow.com/a/76305661/663645
        print(sounddevice.query_devices())

        self.audio = pyaudio.PyAudio()
        self.playing = False # flag to indicate if music is currently playing
        self.play_thread = None # will hold the thread that is playing music
        self._state_lock = threading.Lock() # lock to protect access to the playing flag and play_thread

    #####
    # Name: play_music
    # Purpose: Plays the music, attempting to loop if needed.
    # Arguments: file_path - the path to the music file to be played
    #            start_second - the second in the music file to start playing from
    #            duration - the duration of music to play (0 means play full length)
    #            num_loops - the number of times to loop the music (0 means no loops, play once)
    #####
    def _play_music(self, file_path, start_second, duration, num_loops):
        file_extension = file_path.split(".")[-1]
        if duration == 0.0:
            duration = None

        self.playing = True

        audio_seg = AudioSegment.from_file(
            file=file_path,
            format=file_extension,
            start_second=start_second,
            duration=duration
        )

        stream = self.audio.open(
            format=self.audio.get_format_from_width(audio_seg.sample_width),
            channels=audio_seg.channels,
            rate=audio_seg.frame_rate,
            output=True
        )

        try:
            while self.playing:
                for chunk in make_chunks(audio_seg, 500):
                    if self.playing:
                        stream.write(chunk._data)
                    else:
                        break

                if num_loops > 0:
                    num_loops -= 1
                    if num_loops <= 0:
                        break
        finally:
            stream.stop_stream()
            stream.close()
            self.playing = False

    #####
    # Name: start_music
    # Purpose: This will start playing the specified music file.
    # Arguments: file_path - the path to the music file to be played
    #            start_second - the second in the music file to start playing from
    #            duration - the duration of music to play (0 means play full length)
    #            num_loops - the number of times to loop the music (0 means no loops, play once)
    #####
    def start_music(self, file_path, start_second=0, duration=0.0, num_loops=1):
        self.stop_music(wait=True)

        self.play_thread = threading.Thread(
            target=self._play_music,
            args=(file_path, start_second, duration, float(num_loops)),
            daemon=True
        )
        self.play_thread.start()

    #####
    # Name: stop_music
    # Purpose: This will stop the currently playing music.
    # Arguments: wait - whether to wait for the music to stop
    #            timeout - the maximum time to wait for the music to stop
    #####
    def stop_music(self, wait=False, timeout=None):
        with self._state_lock:
            self.playing = False
            thread = self.play_thread

        if wait and thread is not None and thread.is_alive() and thread is not threading.current_thread():
            thread.join(timeout=timeout)
            return not thread.is_alive()

        return True

    #####
    # Name: destroy
    # Purpose: This will destroy the music player, stopping any currently playing music and terminating the audio.
    # Arguments: none
    #####
    def destroy(self):
        self.stop_music(wait=True)
        self.audio.terminate()


