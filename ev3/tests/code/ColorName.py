#!/usr/bin/env python3
import time
import ev3dev2.sensor as sensor
import ev3dev2.motor as motor
import ev3dev2.sound as sound
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_4
color_sensor = ColorSensor(INPUT_2)
touch_sensor = TouchSensor(INPUT_4)
s = sound.Sound()

from ev3dev2.motor import OUTPUT_B, MediumMotor

motor = MediumMotor(OUTPUT_B)#head turning is C
color_names = {1: 'Black', 2: 'Blue', 3: 'Green', 4: 'Yellow', 5: 'Red', 6: 'White', 7: 'Brown'}

while not touch_sensor.is_pressed:
    color_value = color_sensor.color
    if color_value in color_names:
        motor.on_for_rotations(-50, 0.25)
        s.speak(color_names[color_value])
        time.sleep(0.15)
        motor.on_for_rotations(50, 0.25)
#sudo python3 /home/robot/ev3/ev3/tests/code/ColorName.py