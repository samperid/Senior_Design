#import RPi.GPIO as GPIO
from periphery import GPIO
import time

gpio_out = GPIO(11, "out")

gpio_out.write(True)
time.sleep(5)
gpio_out.write(False)
time.sleep(5)
gpio_out.write(True)
time.sleep(5)
gpio_out.write(False)
time.sleep(5)

'''
GPIO.setup(11, GPIO.OUT)

GPIO.output(11,True) 
time.sleep(5)
GPIO.output(11,False)
time.sleep(5)
GPIO.output(11,True) 
time.sleep(5)
GPIO.output(11,False)
time.sleep(5)
GPIO.output(11,True) 
time.sleep(5)
GPIO.output(11,False)
'''