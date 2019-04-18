import RPi.GPIO as GPIO
from pypylon import pylon

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
#GPIO.output(27, GPIO.HIGH)

tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()

cam.TriggerSelector.SetValue("FrameBurstStart")
cam.TriggerActivation.SetValue("RisingEdge")
cam.TriggerSource.SetValue("Line1")
cam.TriggerMode.SetValue("On")

#cam.TriggerDelayAbs.SetValue(300)