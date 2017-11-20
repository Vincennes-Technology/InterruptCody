#usr/bin/python
#modified by cody purcell  
# script by Alex Eames http://RasPi.tv  

import RPi.GPIO as GPIO
import time
import subprocess
import Adafruit_CharLCD as LCD

logfile = open("LCDDisplay.log", 'a')
lcd = LCD.Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time_stamp = time.time()

def my_callback(channel):
    lcd.clear()
    lcd.message('I am the DM')
def my_callback2(channel):
    lcd.clear()
    lcd.message('I am not the DM')

GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2)
try:
    lcd.clear()
    lcd.message('Are you the DM')
    GPIO.wait_for_edge(24, GPIO.RISING)
    lcd.clear()
    lcd.message('Thank You')
except KeyboardInterrupt:
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
GPIO.cleanup() # clean up GPIO on normal exit
