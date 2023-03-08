#!/usr/bin/env python3

import subprocess
import wave
import pyaudio
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor

# Create a TouchSensor object to detect touch
ts = TouchSensor(INPUT_4)

# Define the audio recording parameters
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk_size = 4096
record_seconds = 10

# Define the filename for the audio recording
filename = "audio.wav"

# Define a function to start recording audio
def start_recording():
    # Define the audio parameters
    audio_format = 'S16_LE'
    channels = 1
    sample_rate = 44100
    chunk_size = 1024

    # Start recording audio using the arecord command
    arecord = subprocess.Popen(['arecord', '-f', audio_format, '-c', str(channels), '-r', str(sample_rate), '-'], stdout=subprocess.PIPE)

    # Write the recorded audio to a WAV file using the soundfile library
    with sf.SoundFile('test.wav', mode='x', samplerate=sample_rate, channels=channels) as file:
        while True:
            # Read a chunk of audio data from arecord
            data = arecord.stdout.read(chunk_size)
            # If there is no more data to read, break out of the loop
            if not data:
                break
            # Write the data to the WAV file
            file.write(data)

    # Close the arecord process
    arecord.terminate()

    print('Recording stopped')


# Define a function to stop recording audio
def stop_recording():
    # Send a SIGINT signal to the arecord subprocess to stop recording
    subprocess.run(['killall', 'arecord'], check=False)

# Define a function to play back the audio
def play_audio():
    # Use the aplay command to play back the audio file
    subprocess.run(['aplay', filename], check=False)

# Main loop
while True:
    # Wait for the touch sensor to be pressed
    while not ts.is_pressed:
        pass
    # Start recording audio
    start_recording()
    # Wait for the touch sensor to be pressed again
    while ts.is_pressed:
        pass
    # Stop recording audio
    stop_recording()
    # Play back the audio
    play_audio()
