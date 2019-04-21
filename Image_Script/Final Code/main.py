from analyze_img import analyze_img
from crop import crop_img
from acquire_img import acquire_img
import RPi.GPIO as GPIO
import time

#Main file which executes separate functions 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
time.sleep(1)

print("Turn on LED")
GPIO.output(27,GPIO.HIGH)
time.sleep(1)

print("Acquiring Image")
acquire_img("410")

#crop_img(file_name)
#analyze_img("patientTest_410")