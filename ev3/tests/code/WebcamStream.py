#!/usr/bin/env python3

# import subprocess
# import os

# image_path = '/home/robot/capture.bmp'  # Path to store the captured image

# def capture_image():
#     subprocess.run(['fswebcam', '-r', '160x90', '--no-banner', image_path])

# def display_image():
#     subprocess.Popen(['brickrun','mplayer', '-vo', 'fbdev2:/dev/fb0', '-framedrop', '-quiet', image_path])

# while True:
#     capture_image()
#     display_image()
import subprocess
import os

image_path = '/home/robot/capture.bmp'  # Path to store the captured image

def capture_image():
    subprocess.run(['fswebcam', '-r', '160x120', '--no-banner', image_path])

def display_image():
    subprocess.Popen(['fbi', '-noverbose', '-T', '1', image_path])

while True:
    capture_image()
    display_image()

#To Run this program, in the ssh do: sudo python3 /home/robot/ev3/ev3/tests/code/WebcamDisplay.py
#Or whatever the path of the pthon program is
# Ctrl+C --> Ctrl+Shift+V
# sudo python3 /home/robot/ev3/ev3/tests/code/WebcamStream.py
#brickrun -- mplayer -fps 15 -demuxer lavf -lavfdopts format=mjpeg -vo fbdev2:/dev/fb0 -quiet /home/robot/webcam.jpg