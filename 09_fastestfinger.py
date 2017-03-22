import RPi.GPIO as GPIO
import  time
from time import sleep
from random import uniform
import subprocess
import os

led1 = 4
#led2 = 24
btn = 23

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
#GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output(led1, GPIO.HIGH)
#GPIO.output(led2, GPIO.HIGH)


sleep (uniform(5,10))

GPIO.output(led1, GPIO.LOW)
#GPIO.output(led2, GPIO.LOW)

start =time.time()
while True:
	if GPIO.input(btn) == False:
		#print("Pin 11 is HIGH")
		
	#else:
    		#print("Pin 11 is LOW")
		break

speed = time.time() - start

print ("Time taken %.4f" % speed  )

GPIO.cleanup
