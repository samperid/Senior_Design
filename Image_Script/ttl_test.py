import RPi.GPIO as GPIO
import time
#hello
GPIO.setmode(GPIO.BCM)

#GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(27, GPIO.HIGH)
time.sleep(15)
GPIO.output(27, GPIO.LOW)
'''
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
GPIO.output(23, GPIO.LOW)
'''