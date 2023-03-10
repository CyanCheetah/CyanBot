#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import ev3dev2.auto as ev3
from time import sleep
import ev3dev2.fonts as fonts
import subprocess
import time
from ev3dev2.sound import Sound
import ev3dev2.sensor as sensor
import subprocess
sound = Sound()


ts = TouchSensor(INPUT_4)
is_recording = False

while True:
    if ts.is_pressed and not is_recording:
        
        cmd = ['arecord', '-D', 'hw:1,0', '-f', 'S16_LE', '-c', '1', '-r', '44100', '/home/robot/myvoice.wav']
        sound.speak('Recording started!')
        recording_process = subprocess.Popen(cmd)
        is_recording = True
    elif ts.is_pressed and is_recording:
        recording_process.terminate()
        sound.speak('Recording stopped!')
        is_recording = False
        break  # exit the loop

    sleep(0.1)

# Play the recorded audio file if the touch sensor is pressed again
if ts.wait_for_pressed():
    subprocess.run(['sudo', 'service', 'udev', 'restart'])
    sound.speak('Playing recorded audio!')
    cmd = ['aplay', '-V', '100', '/home/robot/myvoice.wav']

    subprocess.Popen(cmd).wait()
#sudo python3 /home/robot/ev3/ev3/tests/code/RecordingPlayback.py