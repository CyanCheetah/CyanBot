#!/usr/bin/env python3
import subprocess
import time

# Replace the file path with the path to your MP3 file
mp3_file_path = "/home/robot/ev3/seisyun_complex.mp3"

# Start mpg123 as a subprocess and play the MP3 file
p = subprocess.Popen(["mpg123", "-b", "8192", mp3_file_path])

# Wait for the subprocess to complete
p.wait()
