#!/usr/bin/env python3

from ev3dev2.sound import Sound
import os
import subprocess

# Load video file and get metadata
video_file = "/home/robot/ev3/SeisyunOpening.mp4"
# Use omxplayer to play the video

# Use the omxplayer command to play the video
subprocess.call(["omxplayer", video_file])
Sound().beep()
