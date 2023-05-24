#!/usr/bin/env python3
from ev3dev2.sensor.lego import SoundSensor
from ev3dev2.sensor import INPUT_2, INPUT_1
from ev3dev2.motor import OUTPUT_C, LargeMotor
import time
from time import sleep
import ev3dev2.auto as ev3
from ev3dev2.display import Display
sound_sensor_left = SoundSensor('in2')#left ear is 2
sound_sensor_right = SoundSensor('in1')#right ear is 1
sound_sensor_left.mode = 'DB'
threshold = 92
sound_sensor_right.mode = 'DB'
import ev3dev2.fonts as fonts
motor = LargeMotor(OUTPUT_C)#head turning is C
display = ev3.Display()
MOTOR_SPEED = 50

initial_position = motor.position
target_position = int(360 * .6)#360 is the angle
negtarget_position = int(360 * 1 * -1)#360 is the angle

while True:
    sound_value_left = sound_sensor_left.sound_pressure
    sound_value_right = sound_sensor_right.sound_pressure
    if sound_value_left > threshold:
        motor.run_to_abs_pos(position_sp= int(360 * .8), speed_sp= 50)
        time.sleep(3)
        motor.run_to_abs_pos(position_sp= -int(360 * .8), speed_sp=50)
        motor.wait_until_not_moving()
    elif sound_value_right > threshold:
        motor.run_to_abs_pos(position_sp= -int(360 * .8), speed_sp=50)
        time.sleep(3)
        motor.run_to_abs_pos(position_sp= int(360 * .8), speed_sp=50)
        motor.wait_until_not_moving()
    else:
        motor.stop()



#sudo python3 /home/robot/ev3/ev3/tests/code/Hearing.py