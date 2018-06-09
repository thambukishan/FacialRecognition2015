import io
import time
import cv2
import numpy as np
import PiCamera
import ServoSetup


class OpenCVCapture(object):
	def read(self):
		data = io.BytesIO()
		with picamera.PiCamera() as camera:
			camera.capture(data, format='jpeg')
		data = np.fromstring(data.getvalue(), dtype=np.uint8)
		image = cv2.imdecode(data, 1)
		cv2.imwrite(ServoSetup.DEBUG_IMAGE, image)
		return image
