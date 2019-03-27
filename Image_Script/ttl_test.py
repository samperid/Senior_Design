import RPi.GPIO as GPIO
import time

print("testing script")
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
print(mode)
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print(mode)
'''
GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT)

GPIO.output(0,True) 
time.sleep(5)
GPIO.output(0,False)
time.sleep(5)
GPIO.output(0,True) 
time.sleep(5)
GPIO.output(0,False)
time.sleep(5)
GPIO.output(0,True) 
time.sleep(5)
GPIO.output(0,False)
'''