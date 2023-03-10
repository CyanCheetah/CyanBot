#!/usr/bin/env python3
import subprocess
import time
import threading
from ev3dev2.button import Button

btn = Button()


mp3_file_path = "/home/robot/ev3/seisyun_complex.mp3"
subprocess.Popen(["mpg123", "-b", "8192", mp3_file_path])


        #Ctrl+C --> Ctrl+Shift+V into SSH Terminal
        # sudo python3 /home/robot/ev3/ev3/tests/code/SeisyunComplex.py