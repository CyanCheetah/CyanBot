# EV3-Webcam


This is programming code for the Lego Mindstorms 31313 EV3 kit. Here I will show you how to properly install everything and run webcam software on the EV3 smoothly.

# Table of Contents

* [Installation Guide - EV3DEV](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---ev3dev)
* [Installation Guide - Visual Studio Code](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---visual-studio-code)
* [Installation Guide - Python](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---python)
* [Installation Guide - Visual Studio Code Extensions](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---visual-studio-code-extensions)
* [Installation Guide - CyanBot code into Visual Studio Code](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---cyanbot-code-into-visual-studio-code)
* [Installation Guide - Making Sure EV3DEV is installed](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---making-sure-ev3dev-is-installed)
* [Installation Guide - fswebcam](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---fswebcam)
* [Code File - Webcam.py](https://github.com/CyanCheetah/EV3-Webcam#code-file---webcampy)
* [Installation Guide - fbi (EV3 Display Library)](https://github.com/CyanCheetah/EV3-Webcam#installation-guide---fbi-ev3-display-library)
* [Code File - Webcam Display](https://github.com/CyanCheetah/EV3-Webcam#code-file---webcam-display)
* [Code File - Webcam Stream](https://github.com/CyanCheetah/EV3-Webcam#code-file---webcam-stream)
* [Conclusion](https://github.com/CyanCheetah/EV3-Webcam#conclusion)


# Installation Guide - EV3DEV

First what you want to do is install EV3DEV onto your EV3. 

Here is a link to the official EV3DEV website:
[EV3DEV Installation Guide](https://www.ev3dev.org/docs/getting-started/)

If youtube is more your forte, here is a youtube video on the installation:
[EV3DEV Installation Guide Video](https://www.youtube.com/watch?v=ogLzfo4aYvg&ab_channel=BrandonJacobson)

Once you got the EV3DEV flash screen on your EV3, you should be good to go!

# Installation Guide - Visual Studio Code

Next what you will need is Visual Studio Code. Here we are going to use python as well.

First up, head on over to the Visual Studio website and download the latest release. At the time of writing, I am using Version 1.77

[Visual Studio Code Install](https://code.visualstudio.com/download)

Follow the directions for Visual Studio Code and then launch Visual Studio Code!

# Installation Guide - Python

We are writing our code in Python, specifically Ver. 3.12. It * *Should'nt* * matter what version python you use, though don't quote me on that.

Here is the link to the python download interface:
[Python Download](https://www.python.org/downloads/)

Next what you want to do is open up your Command Prompt and make sure you have Python installed by typing

```
python --version
```

And make sure you get a version number out of it. Your output should look something like this:

```
Python 3.11.2
```

Once you made sure that you have Python installed, you are ready for the next step!

# Installation Guide - Visual Studio Code Extensions

In the sidebar, go to the extensions tab and search up ev3dev-browser. 

![h](https://user-images.githubusercontent.com/91763642/229658655-f3eb5ec4-963e-4894-b44e-38362e8bc897.png)


Once you have installed that, search up Python and install that. This helps by using Intellisense and debug code.

![infogg](https://user-images.githubusercontent.com/91763642/229658672-66ac76cb-9257-44ec-8e47-ddcf9289c1b7.png)


# Installation Guide - CyanBot code into Visual Studio Code

Now we are going to download the code folder and open it in Visual Studio Code.

First up, install the ZIP from GitHub: [Download the ZIP](https://github.com/CyanCheetah/EV3-Webcam/releases/tag/v1.0.0)

Next up, extract the folder by right clicking the folder in your downloads and clicking extract. Once you have, then in Visual Studio Code, you click file > open folder > directory to your folder

Once it is opened, there are a few things we might have to do. 

# Installation Guide - Making Sure EV3DEV is installed

Make sure that the EV3 is in your VS Code
![nb](https://user-images.githubusercontent.com/91763642/229658842-dce1d6a5-a68b-4aa2-8657-b2daef63f635.png)

# Installation Guide - fswebcam

We need to install fswebcam, a linux based webcam program.

fswebcam allows us to access the webcam. First off, make sure you're ev3 is connected via usb and make sure usb webcam is supported by ev3 and plugged into usb port on ev3.

Then in the ev3 ssh terminal, type in:
```bash
sudo apt-get update
```
Then to install fswebcam, run this command in the ssh terminal:
```bash
sudo apt-get install fswebcam
```

We installed fswebcam!

# Code File - Webcam

We can run our first code file: [Webcam.py](https://github.com/CyanCheetah/EV3-Webcam/blob/ev3/ev3/tests/code/Webcam.py)

This code file makes it so that when you hit the touch sensor, then it captures an image and saves it onto the EV3 brick.

Make sure that the Touch Sensor is in the right port, to change it:

```python
from ev3dev2.sensor import INPUT_4
```
Change the input to whatever port number you have it to.

Next up, here is the important command that saves the image:
```python
subprocess.call(['fswebcam', '-r', '100x100', '--no-banner', filename])
```
What this does is saves a 100x100 image onto the ev3 by the name of variable filename

```python
subprocess.call(['fswebcam', '-r', '100x100', '--no-banner', filename])
```
filename:
```python
filename = 'image-{}.jpg'.format(timestamp)
```
You can change the name if you want to. To access it, in VS Code in the ev3dev device browser, check code files it should be saved there.
Usually in:
```
/home/robot/filename
```

# Installation Guide - fbi (EV3 Display Library)

fbi allows us to get images onto ev3 screen

```bash
sudo apt-get update
```

Then

```bash
sudo apt-get install fbi
```

We installed fbi!

# Code File - Webcam Display

Next up is Webcam Display. It basically is the same thing as Webcam but then it displays it. 

WebcamDisplay.py: 
[WebcamDisplay.py](https://github.com/CyanCheetah/EV3-Webcam/blob/ev3/ev3/tests/code/WebcamDisplay.py)

Same thing as Webcam, make sure your touch sensor is in correct port. 

Displays it as:
```bash
subprocess.run(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/image.bmp'])
```

Here is an example:

![f](https://user-images.githubusercontent.com/91763642/229664976-d3550151-50e8-47a4-aae4-75448fb8a11c.png)


# Code File - Webcam Stream

This is the WebcamStream program: [WebcamStream.py](https://github.com/CyanCheetah/EV3-Webcam/blob/ev3/ev3/tests/code/WebcamStream.py)

This is super slow though don't keep you're hopes up.

# Conclusion

That's about it! Any questions, Discord: CyanCheetah#6013


