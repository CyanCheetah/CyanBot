#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor
from ev3dev2.motor import OUTPUT_B, MediumMotor
from ev3dev2.sound import Sound

# Define the B, C, and D motors as LargeMotors
mouth = MediumMotor(OUTPUT_B)
ymotor = LargeMotor(OUTPUT_A)
xmotor = LargeMotor(OUTPUT_D)

# Move the motors to a starting position (optional)

# Speak "Hello! I am CyanBot!"
mouth.on_for_rotations(-50, 0.25)
Sound.speak("Hello! I am CyanBot!").wait()
mouth.on_for_rotations(50, 0.25)
ymotor.on_for_rotations(-100, 1)
ymotor.on_for_rotations(100, 2)
ymotor.on_for_rotations(-100, 1)
xmotor.on_for_rotations(-30, 0.2)
xmotor.on_for_rotations(30, 0.4)
xmotor.on_for_rotations(-30, .2)
mouth.on_for_rotations(-50, 0.25)
Sound.speak("I am a autonomous robot that can perform many tasks.").wait()
mouth.on_for_rotations(50, 0.25)
mouth.on_for_rotations(-50, 0.25)
Sound.speak("I can take pictures, detect color, talk like I am now.").wait()
mouth.on_for_rotations(50, 0.25)
