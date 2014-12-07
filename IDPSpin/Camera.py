import time
import pygame.camera
try:
    import picamera
except:
    "could not start camera"
import io
import base64

class Camera(object):

    def __init__(self):
        try:
            self._Camera = picamera.PiCamera()
            self._Camera.resolution = (640, 480)
            self._Camera.brightness = 50
            self._Camera.start_preview()
            self._StoredImage = ""
        except:
            pass

    
    def takeImage(self, SafeImage=True):
        my_stream = io.BytesIO()
        try:
            self._Camera.capture(my_stream, 'jpeg')
        except:
            pass
        encoded_string = base64.b64encode(my_stream.getvalue())
        if SafeImage:
            self._StoredImage = encoded_string
        return encoded_string

    def getImageFromMemory(self):
        if len(self._StoredImage) > 0:
            return self._StoredImage
        else:
            return self.takeImage(False)

    def Exit(self):
        self._Camera.stop_preview()
        
        
    
