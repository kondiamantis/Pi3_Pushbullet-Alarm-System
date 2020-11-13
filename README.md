# Pi3_Pushbullet-Alarm-System
An IoT implementation of a smart alarm system using Raspberry Pi 3.

This project was created for my Thesis at University of Pireays, Department of Digital Systems.

It's a project that gives people the ability to build their own inexpensive, expandable and feature-rich alarm system.
Pushbullet API was also used to push a notification ( including an image of the intruder ) whenever the alarm system detects movement.

The project includes:
PIR Sensor
Pi Camera
LCD Display
LED controllable lights
Push Buttons
Resistors

It's a great project to have a first touch with GPIOs pins and modules.

For the connection with the Pushbullet API the user must create a unique API KEY and place it in the variable API_KEY. Then, he can connect his code with every device he has pushbullet connected with his account.

The programm needs the 2 files in the same folder so it can run properly because these are the drivers for the display.
