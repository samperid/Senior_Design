from pypylon import pylon
import platform

def acquire_img(img_name):
    #Define camera values 
    path = "../../Images/"
    img = pylon.PylonImage()
    tlf = pylon.TlFactory.GetInstance()
    cam = pylon.InstantCamera(tlf.CreateFirstDevice())
    cam.Open()

    #Define trigger settings for camera 
    cam.TriggerSelector.SetValue("FrameBurstStart")
    cam.TriggerSource.SetValue("Software")
    cam.TriggerMode.SetValue("On")

    #Can use StartGrabbing()/StopGrabbing() method to switch on/off triggering execution
    #Will only execute if software trigger is run
    cam.StartGrabbing()
    cam.TriggerSoftware.Execute()
    #RetrieveResult(timeout before image is taken)
    #Can adjust for acquisition time and TTL pulse time delays 
    with cam.RetrieveResult(2000) as result:
        # Calling AttachGrabResultBuffer creates another reference to the
        # grab result buffer. This prevents the buffer's reuse for grabbing.
        img.AttachGrabResultBuffer(result)
        filename = "%s.png" % img_name
        img.Save(pylon.ImageFileFormat_Png, path+filename)

        # In order to make it possible to reuse the grab result for grabbing
        # again, we have to release the image (effectively emptying the
        # image object).
        img.Release()

    cam.StopGrabbing()
    cam.Close()

