#!/usr/bin/env python3
import subprocess
for i in range(50):
    subprocess.run(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/ev3/SeisyunOpening_000/SeisyunOpening_'+str(i).zfill(3)+'.jpg'])
# sudo python3 /home/robot/ev3/ev3/tests/code/Blend2.py