#!/usr/bin/env python3
import subprocess

video_path = "/home/robot/ev3/Video.gif"

# Build the command to play the video
command = ["sudo", "fbi", "-noverbose", "-T", "1", "-a", video_path]

# Execute the command
process = subprocess.Popen(command)

# Wait for the process to finish
process.wait()

#sudo python3 /home/robot/ev3/ev3/tests/code/Vid.py