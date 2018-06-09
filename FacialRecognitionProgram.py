#Implemented in Box to be ran, acts as user interface for project
import cv2
import ServoSetup
import OpenCVimplementation
import HardwareCode


if __name__ == '__main__':
    #Intializes Training Data
	print 'Training Data is Loading...'
	model = cv2.createFisherFaceRecognizer()
	model.load(ServoSetup.TRAINING_FILE)
	print 'Training data successfully loaded'
	camera = ServoSetup.get_camera()
	box = HardwareCode.Box()
	#Makes box lock
	box.lock()
	print 'Running Program'
	print 'Press button to lock (if unlocked), or unlock if the correct face is detected.'
	print 'Ctrl-C to quit program'
	while True:
		if box.is_button_up():
			if not box.is_locked:
                #Lock the box if it is unlocked
				box.lock()
				print 'Box is locked'
			else:
				print 'Button pressed, looking for face...'
				#Check for the positive face and unlock if found
				image = camera.read()
				#Grayscales Image
				image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
				#Graphically maps of face in image with coordinates
				result = OpenCVimplementation.detect_single(image)
				if result is None:
					print 'Could not detect face. Reference debugimage.pgm for debug'
					continue
				x, y, w, h = result
				crop = OpenCVimplementation.resize(OpenCVimplementation.crop(image, x, y, w, h))
				label, confidence = model.predict(crop)
				print 'Predicted {0} face with confidence {1} (lower is more confident).'.format(
					'POSITIVE' if label == ServoSetup.POSITIVE_LABEL else 'NEGATIVE',
					confidence)
				if label == ServoSetup.POSITIVE_LABEL and confidence < ServoSetup.POSITIVE_THRESHOLD:
					print 'Face recognized'
					box.unlock()
				else:
					print 'Did not recognize face'
