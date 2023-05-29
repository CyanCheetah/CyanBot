#!/usr/bin/env python3

import subprocess
import time
# Set the path to the directory containing the images
image_directory = "/home/robot/ev3/ylia"


def configure_framebuffer():
    # Configure the framebuffer settings to minimize black frames
    subprocess.call(["fbset", "-depth", "8"])
    subprocess.call(["fbset", "-rgba", "8/0,8/0,8/0,8/0"])

def display_images():
    # Get a list of all image files in the directory
    image_files = subprocess.check_output(["ls", image_directory]).decode().split()

    # Iterate through each image file and display it using fbi
    for image_file in image_files:
        subprocess.call(["fbi", "-noverbose", "-T", "1", "-a", image_directory + "/" + image_file])


if __name__ == "__main__":
    configure_framebuffer()
    display_images()

#sudo python3 /home/robot/ev3/ev3/tests/code/ylia.py
