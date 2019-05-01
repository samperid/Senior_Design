from analyze_img import analyze_img
from crop import crop_img
from acquire_img import acquire_img
import RPi.GPIO as GPIO
import time

#Main file which executes separate functions 
def main(name):
	name = str(name)
	#Assign GPIO information
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#410nm
	GPIO.setup(4,GPIO.OUT)
	#490nm
	GPIO.setup(27,GPIO.OUT)
	#565nm
	GPIO.setup(22,GPIO.OUT)
	#625nm
	GPIO.setup(24,GPIO.OUT)
	#730nm
	GPIO.setup(25,GPIO.OUT)
	#808nm
	GPIO.setup(5,GPIO.OUT)
	#940
	GPIO.setup(6,GPIO.OUT)

	GPIO.output(4,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(6,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	#Acquire each individual image per wavelength 
	print("Turn on 410nm LED")
	GPIO.output(4,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 410nm Image")
	file_name = name+"_410"
	acquire_img(file_name)
	GPIO.output(4,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	print("Turn on 490nm LED")
	GPIO.output(27,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 490nm Image")
	file_name = name+"_490"
	acquire_img(file_name)
	GPIO.output(27,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	print("Turn on 565nm LED")
	GPIO.output(22,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 565nm Image")
	file_name = name+"_565"
	acquire_img(file_name)
	GPIO.output(22,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(0.5)

	print("Turn on 625nm LED")
	GPIO.output(24,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 625nm Image")
	file_name = name+"_625"
	acquire_img(file_name)
	GPIO.output(24,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	print("Turn on 730nm LED")
	GPIO.output(25,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 730nm Image")
	file_name = name+"_730"
	acquire_img(file_name)
	GPIO.output(25,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	print("Turn on 808nm LED")
	GPIO.output(5,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 808nm Image")
	file_name = name+"_808"
	acquire_img(file_name)
	GPIO.output(5,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	print("Turn on 940nm LED")
	GPIO.output(6,GPIO.HIGH)
	# time.sleep(0.5)
	time.sleep(1)

	print("Acquiring 940nm Image")
	file_name = name+"_940"
	acquire_img(file_name)
	GPIO.output(6,GPIO.LOW)
	# time.sleep(0.5)
	time.sleep(1)

	#crop_img(file_name)
	#analyze_img("patientTest_410")
