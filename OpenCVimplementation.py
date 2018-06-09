import cv2
import ServoSetup

haar_faces = cv2.CascadeClassifier(ServoSetup.HAAR_FACES)
#Defines image resizing
def resize(image):
    return cv2.resize(image,
                      (ServoSetup.FACE_WIDTH, ServoSetup.FACE_HEIGHT),
                      interpolation=cv2.INTER_LANCZOS4)
#Defines face detection
def detect_single(image):
	faces = haar_faces.detectMultiScale(image, 
				scaleFactor=ServoSetup.HAAR_SCALE_FACTOR, 
				minNeighbors=ServoSetup.HAAR_MIN_NEIGHBORS, 
				minSize=ServoSetup.HAAR_MIN_SIZE, 
				flags=cv2.CASCADE_SCALE_IMAGE)
	if len(faces) != 1:
		return None
	return faces[0]
#Defines image cropping
def crop(image, x, y, w, h):
	crop_height = int((ServoSetup.FACE_HEIGHT / float(ServoSetup.FACE_WIDTH)) * w)
	midy = y + h/2
	y1 = max(0, midy-crop_height/2)
	y2 = min(image.shape[0]-1, midy+crop_height/2)
	return image[y1:y2, x:x+w]
