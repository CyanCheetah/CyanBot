#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, MediumMotor
import time
from time import sleep
import ev3dev2.auto as ev3
from ev3dev2.display import Display

motor = MediumMotor(OUTPUT_B)#head turning is C

from ev3dev2.sound import Sound
import ev3dev2.sensor as sensor
import subprocess
sound = Sound()

target_position = int(360 * .6)#360 is the angle
negtarget_position = int(360 * 1 * -1)#360 is the angle
motor.run_to_abs_pos(position_sp= int(360 * -1.5), speed_sp= 50)
sound.speak('Hello. I am CyanBot. I was created by CyanCheetah. I can do many things. I am using Ee Vee 3 dev and am programmed using the Python language. I can see, listen, and function like a regular human!')


#sudo python3 /home/robot/ev3/ev3/tests/code/Hearing.py