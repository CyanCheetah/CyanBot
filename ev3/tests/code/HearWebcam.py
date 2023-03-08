#!/usr/bin/env python3

import os
import subprocess
import ev3dev2.sensor.lego as sensors
import time

# Configure the USB webcam
subprocess.call(["sudo", "modprobe", "uvcvideo"])
subprocess.call(["sudo", "v4l2-ctl", "-d", "/dev/video0", "-c", "exposure_auto=1"])
subprocess.call(["sudo", "v4l2-ctl", "-d", "/dev/video0", "-c", "exposure_absolute=50"])

# Set up the Sound sensor
sound = sensors.Sound()

# Define a function to take a picture using fswebcam
def take_picture():
    subprocess.call(["fswebcam", "-r", "640x480", "picture.jpg"])

# Wait for sound and take a picture
while True:
    if sound.wait_until_pressed():
        take_picture()
        time.sleep(1) # Wait for 1 second to avoid taking multiple pictures in quick succession
