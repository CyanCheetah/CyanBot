#!/usr/bin/env python3
import subprocess
import time
# Run the `sudo fbi` command to display an image
#img.bmp
#ha.bmp
filename = 'img.bmp'
subprocess.run(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/ev3/ha.bmp'])

time.sleep(5)


#To Run this program, in the ssh do: sudo python3 /home/robot/ev3/ev3/tests/code/Display.py
#Or whatever the path of the pthon program is
