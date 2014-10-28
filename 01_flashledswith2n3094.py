# leds.py
# flash leds vi NPN transistor like 2n3904

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 22
led_pause = 0.2

GPIO.setup(led_pin, GPIO.OUT)

try:         
    while True:
        GPIO.output(led_pin, True)
        time.sleep(led_pause)
        GPIO.output(led_pin, False)
        time.sleep(led_pause)
finally:  
    print("Cleaning up")
    GPIO.cleanup()
