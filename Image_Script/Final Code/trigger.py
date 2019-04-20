import RPi.GPIO as GPIO
from pypylon import pylon
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()

#cam.TriggerActivation.SetValue("FrameBurstStart")
cam.TriggerSource.SetValue("Line1")
cam.TriggerMode.SetValue("On")
#cam.TriggerActivation.SetValue("RisingEdge")



#cam.AcquisitionStatusSelector.SetValue("FrameStart")
#isWaitingForFrameStart = cam.AcquisitionStatus.GetValue()

'''
for i in range(0,4):
	if i % 2 == 0:
		GPIO.output(27, GPIO.HIGH)
		if(isWaitingForFrameStart):
			#it is now safe to apply frame start trigger signals
			cam.TriggerSelector.SetValue("FrameStart")
	time.sleep(1)
#cam.TriggerDelayAbs.SetValue(300)
'''