#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2
import os
from ev3dev2.motor import OUTPUT_B
import time
import ev3dev2.sensor as sensor
import ev3dev2.motor as motor
import ev3dev2.sound as sound
from ev3dev2.sound import Sound

from ev3dev2.sensor.lego import ColorSensor
# Initialize color sensor on port 2
color_sensor = ColorSensor(INPUT_2)
m = motor.LargeMotor(OUTPUT_B)
# Initialize Sound object
s = sound.Sound()

# Define a dictionary of color values and their corresponding names
color_names = {
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown'
}

# Loop forever
while True:
    # Read color sensor value
    color_value = color_sensor.color

    # Check if the color is in the dictionary
    if color_value in color_names:
        # Speak the color name out loud
        

        # Move the motor for .15 rotations at 20 speed
        m.on_for_rotations(-50, 0.25)
        s.speak(color_names[color_value])
        # Sleep for .3 seconds
        time.sleep(0.15)

        # Move the motor back to the original position
        m.on_for_rotations(50, 0.25)
        

