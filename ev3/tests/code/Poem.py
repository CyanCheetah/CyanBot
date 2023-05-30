#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, MediumMotor
import time
from time import sleep
import ev3dev2.auto as ev3
from ev3dev2.display import Display
import threading
motor = MediumMotor(OUTPUT_B)#head turning is C

from ev3dev2.sound import Sound
import ev3dev2.sensor as sensor
import subprocess

sound = Sound()

target_position = int(360 * .6)
negtarget_position = int(360 * 1 * -1)

def play_sound_and_move_motor(speed, rotations, text):
    t = threading.Thread(target=sound.speak, args=(text,))
    motor.on_for_rotations(speed, -rotations)
    t.start()
    t.join()
    motor.on_for_rotations(speed, rotations)

play_sound_and_move_motor(50, .3, 'Hello. I am CyanBot. I was created by CyanCheetah. ')

play_sound_and_move_motor(50, .3, 'I can do many things. ')
play_sound_and_move_motor(50, .3, 'I am using Ee Vee 3 dev and am programmed using the Python language.')
play_sound_and_move_motor(50, .3, 'I can see, listen, and function like a regular human!')
play_sound_and_move_motor(50, .3, 'Since this is English class,')
play_sound_and_move_motor(50, .3, 'I wanted to do something that is related to english')
play_sound_and_move_motor(50, .3, 'So I will be reading a short poem on a topic we are doing in class')

play_sound_and_move_motor(50, .3, 'I will be reading a Harlem Renaissance Poem.')
play_sound_and_move_motor(50, .3, 'I, Too. By Langston Hughes')
play_sound_and_move_motor(50, .3, 'I, too, sing America. I am the darker brother.')
play_sound_and_move_motor(50, .3, 'They send me to eat in the kitchen When company comes,')
play_sound_and_move_motor(50, .3, 'But I laugh, And eat well, And grow strong.')
play_sound_and_move_motor(50, .3, 'Tomorrow, I l be at the table When company comes.')
play_sound_and_move_motor(50, .3, 'Nobody l dare Say to me, Eat in the kitchen, Then.')
play_sound_and_move_motor(50, .3, 'Besides, They l see how beautiful I am And be ashamed')
play_sound_and_move_motor(50, .3, 'I, too, am America.')

#sudo python3 /home/robot/ev3/ev3/tests/code/Poem.py