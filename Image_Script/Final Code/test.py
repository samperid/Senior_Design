import RPi.GPIO as GPIO
import time
from pypylon import pylon
import platform
from acquire_img import acquire_img

filenames = ["test1","test2","test3"]

for name in filenames:
	acquire_img(name)


'''
cam.StartGrabbing()
for i in range(num_img_to_save):
	#RetrieveResult(timeout before image is taken)
	#Can adjust for acquisition time and TTL pulse time delays
	if i == 0:
	    with cam.RetrieveResult(2000) as result:
	    	
	        # Calling AttachGrabResultBuffer creates another reference to the
	        # grab result buffer. This prevents the buffer's reuse for grabbing.
	        GPIO.output(27,GPIO.HIGH)
	        time.sleep(1)
	        img.AttachGrabResultBuffer(result)
	        filename = "saved_pypylon_img_%d.png" % i
	        img.Save(pylon.ImageFileFormat_Png, path+filename)
	        # In order to make it possible to reuse the grab result for grabbing
	        # again, we have to release the image (effectively emptying the
	        # image object).
	        img.Release()
	        GPIO.output(27,GPIO.LOW)
	else:
		with cam.RetrieveResult(2000) as result:
			#GPIO.output(27,GPIO.HIGH)
			time.sleep(1)
			img.AttachGrabResultBuffer(result)
			filename = "saved_pypylon_img_%d.png" % i
			img.Save(pylon.ImageFileFormat_Png, path+filename)
			#GPIO.output(27,GPIO.LOW)

		    # In order to make it possible to reuse the grab result for grabbing
		    # again, we have to release the image (effectively emptying the
		    # image object).img.Release()

cam.StopGrabbing()
cam.Close()
'''