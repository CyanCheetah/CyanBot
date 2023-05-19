#!/usr/bin/env python3
import subprocess
import time

def display_images():
    image_files = subprocess.check_output(["ls", "/home/robot/ev3/mp4_000"]).decode().split()

    for image_file in image_files:
        subprocess.call(["mplayer", "/home/robot/ev3/mp4_000" + "/" + image_file, "-vo", "fbdev2:/dev/fb0", "-framedrop"])

if __name__ == "__main__":
    display_images()

#sudo python3 /home/robot/ev3/ev3/tests/code/Blend.py
