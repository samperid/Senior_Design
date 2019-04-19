import RPi.GPIO as GPIO
from pypylon import pylon

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
#GPIO.output(27, GPIO.HIGH)

tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()

cam.TriggerSelector.SetValue("FrameStart")
cam.TriggerActivation.SetValue("RisingEdge")
cam.TriggerSource.SetValue("Line1")
cam.TriggerMode.SetValue("On")
cam.AcquisitionStatusSelector.SetValue("FrameStart")

bool isWaitingForFrameStart = cam.AcquisitionStatus.GetValue()

if(isWaitingForFrameStart){
	#it is now safe to apply frame start trigger signals
}

#cam.TriggerDelayAbs.SetValue(300)