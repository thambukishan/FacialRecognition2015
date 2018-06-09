import glob
import os
import sys
import select
import cv2
import HardwareCode
import ServoSetup
import OpenCVimplementation

POSITIVE_FILE_PREFIX = 'positive_'

def is_letter_input(letter):
	if select.select([sys.stdin,],[],[],0.0)[0]:
		input_char = sys.stdin.read(1)
		return input_char.lower() == letter.lower()
	return False


if __name__ == '__main__':
	camera = ServoSetup.get_camera()
	box = HardwareCode.Box()
	#New directory for positive training images if none is there
	if not os.path.exists(ServoSetup.POSITIVE_DIR):
		os.makedirs(ServoSetup.POSITIVE_DIR)
	files = sorted(glob.glob(os.path.join(ServoSetup.POSITIVE_DIR, 
		POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
	count = 0
	if len(files) > 0:
		count = int(files[-1][-7:-4])+1
	print 'Capturing positive training images'
	print 'Press button to capture an image'
	print 'Press Ctrl-C to quit.'
	while True:
		#Checks button pressed
		if box.is_button_up()
			print 'Taking image...'
			image = camera.read()
			#Convert image to grayscale.
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			#Gets coordinates of face in captured image
			result = OpenCVimplementation.detect_single(image)
			if result is None:
				print 'Could not detect face.  Check debugimage.pgm for debug'
				continue
			x, y, w, h = result
			#Crop image to usuable resolution
			crop = OpenCVimplementation.crop(image, x, y, w, h)
			#Image saved
			filename = os.path.join(ServoSetup.POSITIVE_DIR, POSITIVE_FILE_PREFIX + '%03d.pgm' % count)
			cv2.imwrite(filename, crop)
			print 'Took training image', filename
			count += 1
