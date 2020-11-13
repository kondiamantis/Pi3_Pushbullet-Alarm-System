# -*- coding: utf-8 -*-
#It is written in python 2.7 or else the pushbullet package presents errors
#IMPORTANT NOTE-If there is open any other python shell the camera presents errors
  
import RPi.GPIO as GPIO
import time
import lcddriver
from picamera import PiCamera
from pushbullet import Pushbullet


API_KEY = 'YOUR PUSHBULLET API KEY'
pb=Pushbullet(API_KEY)
display=lcddriver.lcd()
camera=PiCamera()
CurrentPIRState=False
inputButtonState=True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #reads the pins with their number not with their name like GPIO.BCM
GPIO.setup(11, GPIO.IN, GPIO.PUD_DOWN) #PIR Sensor
GPIO.setup(37,GPIO.OUT) #LED output pin
GPIO.setup(15, GPIO.OUT) #Buzzer pin
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button pin

def buzzerSounds():        
            #Dot Dot Dot
            GPIO.output(15, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(15, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(15, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(15, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(15, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(15, GPIO.LOW)
            time.sleep(0.2)
       


def sendImage():
        with open("/home/pi/Desktop/image.jpg","rb") as pic:
                fileData=pb.upload_file(pic, "image.jpg")
                
        pb.push_file(**fileData)



def snapshot(): #wait 3 seconds and then take a snapshot of the intruder
        
        camera.resolution=(1024,768)
        camera.start_preview()
        time.sleep(3)
        camera.capture("/home/pi/Desktop/image.jpg")
        camera.stop_preview()
        


print ("Waiting for motion detection")

try:
        while inputButtonState==True:
                
                CurrentPIRState=GPIO.input(11)
                inputButtonState=GPIO.input(12)
                if CurrentPIRState == True: #when input from PIR sensor is high
                        print("Motion detected")
                        buzzerSounds()
                        GPIO.output(37,1) #Turn on LED
                        time.sleep(1)
                        GPIO.output(37,0) #Turn of LED
                        
                        localTime=time.strftime("%H:%M:%S") #24-hour format
                        display.lcd_display_string("Motion detection ",1) #1st line of lcd
                        display.lcd_display_string(localTime,2) #2nd line of lcd
                        
                           
                        #take a snapshot of the intruder
                        snapshot()
                        
                        #send notification 
                        pb.push_note("Συναγερμός!!!", "Ανιχνεύθηκε κίνηση στο δωμάτιο")

                        #send notification with image to my smartphone
                        sendImage()
                        
                        

                        
except KeyboardInterrupt:
    display.lcd_display_string("Cleaning up",1)
    time.sleep(1) 
    display.lcd_clear()
		
		
