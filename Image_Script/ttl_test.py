import RPi.GPIO as GPIO
import time

print("testing script")
GPIO.setmode(GPIO.BCM)

ttl_pin = 11

GPIO.setup(ttl_pin, GPIO.OUT)

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