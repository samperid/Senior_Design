import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)

GPIO.output(14, GPIO.LOW)
time.sleep(3)
GPIO.output(14, GPIO.HIGH)
time.sleep(3)
GPIO.output(14, GPIO.LOW)
time.sleep(3)
GPIO.output(14, GPIO.HIGH)
time.sleep(3)
GPIO.output(14, GPIO.LOW)
time.sleep(3)
GPIO.output(14, GPIO.HIGH)
time.sleep(3)
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