from ev3dev2.display import Display
from ev3dev2 import ev3
import subprocess

# Create an instance of the EV3 screen
screen = Display()

# Execute the brickrun command and capture the output
process = subprocess.Popen(
    ['brickrun', '--', 'mpg123', '-@', 'http://us3.streamingpulse.com:7015/live', '-b', '100000'],
    stdout=subprocess.PIPE,
    universal_newlines=True
)

# Loop through the output of the command
for line in iter(process.stdout.readline, ''):
    # Check if the line contains the station name
    if 'ICY-NAME' in line:
        station_name = line.split('ICY-NAME: ')[1].strip()
        screen.draw.text((10, 10), f"Station:"+station_name)
        screen.update()

    # Check if the line contains the song name
    if 'ICY-META: StreamTitle' in line:
        song_name = line.split("StreamTitle='")[1].split("';")[0]
        screen.draw.text((10, 50), f"Song: {song_name}")
        screen.update()

    # Check if the middle button is pressed
    if ev3.Button().middle:
        break

# Close the subprocess
process.stdout.close()
process.wait()
#sudo python3 /home/robot/ev3/ev3/tests/code/Radio.py
# brickrun -- /home/robot/ev3/ev3/tests/code/Radio.py
#brickrun -- mpg123 -l 1 --loop -1 -@ http://icecast.omroep.nl/radio1-bb-mp3 -b 1024


#brickrun -- mpg123 -@ http://us3.streamingpulse.com:7015/live -b 100000
#brickrun -- mpg123 -@ "http://91.232.4.33:7028/stream?type=http&nocache=185776" -l 1

#brickrun -- mplayer -afm mp3lib -acodec mp3 -bps 128 -srate 44100 "http://91.232.4.33:7028/stream?type=http&nocache=185776"


#brickrun -- mplayer /home/robot/ev3/Chika-Dance.mp4 -vo fbdev2:/dev/fb0 -framedrop
#brickrun -- mplayer /home/robot/ev3/output_file.mp4 -vo fbdev2:/dev/fb0 -framedrop
#brickrun -- mplayer /home/robot/ev3/YourNameScenery.gif -vo fbdev2:/dev/fb0 -framedrop
#brickrun -- mpg123 /home/robot/ev3/BadAppleSong.mp3
#brickrun -- mplayer /home/robot/ev3/output_file.mp4 --autosync 5vo fbdev2:/dev/fb0 -framedrop
#brickrun -- ffmpeg -i /home/robot/ev3/BadAppleSong.mp3 /home/robot/ev3/BadAppleSong.wav
#brickrun -- mpg123 /home/robot/ev3/BadAppleSong.mp3 -b 10000
#brickrun -- aplay /home/robot/ev3/BadAppleSong.wav


#brickrun -- mplayer /home/robot/ev3/BadApple.mp4 -ao sdl -vo fbdev2:/dev/fb0 -autosync 5 -vfm ffmpeg -lavdopts lowres=1:fast:skiploopfilter=all -cache 16000 -nocache
#brickrun -- mplayer /home/robot/ev3/BadApple.mp4 -framedrop -vo fbdev2:/dev/fb0 -autosync 5
#brickrun -- mplayer /home/robot/ev3/output_file.mp4 -framedrop -vo fbdev2:/dev/fb0 -autosync 5 -vfm ffmpeg -lavdopts lowres=1:fast:skiploopfilter=all -cache 16000 -nocache

#brickrun -- mplayer /home/robot/ev3/BadApple.mp4 -vo fbdev2:/dev/fb0 -autosync 100
#ffmpeg -i /home/robot/ev3/BadAppleSong.wav -ac 1 -ar 16000 /home/robot/ev3/output.wav
#ffmpeg -i /home/robot/ev3/BadApple.mp4 -i /home/robot/ev3/BadAppleSong.wav -c:v copy -c:a copy /home/robot/ev3/output_file.mp4