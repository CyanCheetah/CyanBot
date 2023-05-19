#!/usr/bin/env python3
import subprocess
import io
import os
from ev3dev2.sensor import INPUT_4
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import openai
import time

from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import TouchSensor

sound = Sound()
touch_sensor = TouchSensor(INPUT_4)

def record_audio():
    subprocess.call("arecord -D hw:1,0 -f S16_LE -r 16000 voice.wav", shell=True)

def transcribe_audio():
    client = speech.SpeechClient()
    with io.open("voice.wav", "rb") as audio_file:
        content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        model="video"
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)
    return response.results[0].alternatives[0].transcript

def generate_response(text):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    prompt = "Your prompt here: {}".format(text)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def speak_response(response):
    sound.speak(response)

recording = False

while True:
    if touch_sensor.is_pressed and not recording:
        sound.beep()
        recording = True
        record_audio()
    elif touch_sensor.is_pressed and recording:
        sound.beep()
        text = transcribe_audio()
        print("You said: {}".format(text))

        response = generate_response(text)
        print("GPT Says: {}".format(response))

        speak_response(response)
        recording = False
    time.sleep(0.1)
#sudo python3 /home/robot/ev3/ev3/tests/code/Talking.py