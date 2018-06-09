#Pi_GPIO port which is connected to the lock servo
LOCK_SERVO_PIN = 18
#Value set in microseconds for the servo at the unlocked and locked states
LOCK_SERVO_UNLOCKED = 2000
LOCK_SERVO_LOCKED   = 1100

#Pi_GPIO port number
BUTTON_PIN = 25
BUTTON_DOWN = False  #Low signal
BUTTON_UP   = True   # High signal

#Threshold for positive match; important for success rate
POSITIVE_THRESHOLD = 2000.0
TRAINING_FILE = 'training.xml'

#Directories for positive and negative training images
POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'

POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2

#Size of control set of images
FACE_WIDTH  = 92
FACE_HEIGHT = 112
HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

DEBUG_IMAGE = 'debugimage.pgm'

def get_camera():
	import picam
	return picam.OpenCVCapture()
