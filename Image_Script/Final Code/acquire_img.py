"""This sample shows how grabbed images can be saved using pypylon only (no
need to use openCV).

Available image formats are     (depending on platform):
 - pylon.ImageFileFormat_Bmp    (Windows)
 - pylon.ImageFileFormat_Tiff   (Linux, Windows)
 - pylon.ImageFileFormat_Jpeg   (Windows)
 - pylon.ImageFileFormat_Png    (Linux, Windows)
 - pylon.ImageFileFormat_Raw    (Windows)
"""
from pypylon import pylon
import platform

path = "../Images/"
num_img_to_save = 2
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()

cam = pylon.InstantCamera(tlf.CreateFirstDevice())
cam.Open()
cam.StartGrabbing()
for i in range(num_img_to_save):
	#RetrieveResult(timeout before image is taken)
	#Can adjust for acquisition time and TTL pulse time delays 
    with cam.RetrieveResult(2000) as result:

        # Calling AttachGrabResultBuffer creates another reference to the
        # grab result buffer. This prevents the buffer's reuse for grabbing.
        img.AttachGrabResultBuffer(result)
        filename = "saved_pypylon_img_%d.png" % i
        img.Save(pylon.ImageFileFormat_Png, path+filename)

        # In order to make it possible to reuse the grab result for grabbing
        # again, we have to release the image (effectively emptying the
        # image object).
        img.Release()

cam.StopGrabbing()
cam.Close()
