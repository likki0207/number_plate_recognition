# Number plate recognition:
Detects license plate of car and recognizes its characters

# Packages required:
-> opencv : OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, 
it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source BSD license.

# Installing the packages:
-> pip install opencv -python

# Description
In this project we have used the haarcascade_russian_plate_number.xml; 
A Haar Cascade is basically a classifier which is used to detect the object for which it has been trained for, from the source. 
The Haar Cascade is trained by superimposing the positive image over a set of negative images. 
The training is generally done on a server and on various stages.

# Working:
![](video-working.gif)

# Execution:
python number_plate_recognition.py
