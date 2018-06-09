import fnmatch
import os
import cv2
import numpy as np
import ServoSetup
import OpenCVimplementation


MEAN_FILE = 'mean.png'
POSITIVE_FISHERFACE_FILE = 'positive_fisherface.png'
NEGATIVE_FISHERFACE_FILE = 'negative_fisherface.png'


def walk_files(directory, match='*'):
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

def prepare_image(filename):
	return face.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype=None):
	X = np.asarray(X)
	minX, maxX = np.min(X), np.max(X)
	X = X - float(minX)
	X = X / float((maxX - minX))
	X = X * (high-low)
	X = X + low
	if dtype is None:
		return np.asarray(X)
	return np.asarray(X, dtype=dtype)

if __name__ == '__main__':
	print 'Reading training images...'
	faces = []
	labels = []
	pos_count = 0
	neg_count = 0
	for filename in walk_files(ServoSetup.POSITIVE_DIR, '*.pgm'):
		faces.append(prepare_image(filename))
		labels.append(ServoSetup.POSITIVE_LABEL)
		pos_count += 1
	for filename in walk_files(ServoSetup.NEGATIVE_DIR, '*.pgm'):
		faces.append(prepare_image(filename))
		labels.append(ServoSetup.NEGATIVE_LABEL)
		neg_count += 1
	print 'Read', pos_count, 'positive images and', neg_count, 'negative images.'

	print 'Training model...'
	model = cv2.createFisherFaceRecognizer()
	model.train(np.asarray(faces), np.asarray(labels))

	model.save(ServoSetup.TRAINING_FILE)
	print 'Training data saved to', ServoSetup.TRAINING_FILE

	mean = model.getMat("mean").reshape(faces[0].shape)
	cv2.imwrite(MEAN_FILE, normalize(mean, 0, 255, dtype=np.uint8))
	fishervectors = model.getMat("fishervectors")
	pos_fishervector = fishervectors[:,0].reshape(faces[0].shape)
	cv2.imwrite(POSITIVE_FISHERFACE_FILE, normalize(pos_fishervector, 0, 255, dtype=np.uint8))
	neg_fishervector = fishervectors[:,1].reshape(faces[0].shape)
	cv2.imwrite(NEGATIVE_FISHERFACE_FILE, normalize(neg_fishervector, 0, 255, dtype=np.uint8))
