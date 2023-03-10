#!/usr/bin/env python3

import time
import ev3dev2.auto as ev3
import ev3dev2.fonts as fonts
import subprocess
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from multiprocessing import Process

btn = Button()
sound = Sound()
screen = ev3.Display()
screen.clear()


sound.speak('Hello! This is a streaming program. This will stream the photos to the ev3 screen.')



def capture_image():
    while not btn.down:
        subprocess.call(['fswebcam', '-r', '50x50', '--no-banner', 'image.bmp'])


def display_image():
    while not btn.down:
        subprocess.Popen(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/image.bmp'])


if __name__ == '__main__':
    p1 = Process(target=capture_image)
    p2 = Process(target=display_image)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

#To Run this program, in the ssh do: sudo python3 /home/robot/ev3/ev3/tests/code/WebcamDisplay.py
#Or whatever the path of the pthon program is
# Ctrl+C --> Ctrl+Shift+V
# sudo python3 /home/robot/ev3/ev3/tests/code/WebcamStream.py
