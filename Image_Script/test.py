import RPi.GPIO as GPIO
import time
from pypylon import pylon
import platform

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)

path = "../Images/"
num_img_to_save = 2
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()

cam.TriggerSelector.SetValue("FrameBurstStart")
cam.TriggerSource.SetValue("Software")
cam.TriggerMode.SetValue("On")

cam.StartGrabbing()
#cam.TriggerSoftware.Execute()
with cam.RetrieveResult(2000) as result:
	
    # Calling AttachGrabResultBuffer creates another reference to the
    # grab result buffer. This prevents the buffer's reuse for grabbing.
	img.AttachGrabResultBuffer(result)
	filename = "trigger_capture.png"
	img.Save(pylon.ImageFileFormat_Png, path+filename)

    # In order to make it possible to reuse the grab result for grabbing
    # again, we have to release the image (effectively emptying the
    # image object).
	img.Release()

cam.StopGrabbing()
cam.Close()


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