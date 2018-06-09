import time
import cv2
import RPIO
from RPIO import PWM
import BoxCamera
import ServoSetup
import OpenCVimplementation


class Box(object):
	def __init__(self):
		self.servo = PWM.Servo()
		RPIO.setup(ServoSetup.BUTTON_PIN, RPIO.IN)
		self.button_state = RPIO.input(ServoSetup.BUTTON_PIN)
		self.is_locked = None
    #Defines Lock
	def lock(self):
		self.servo.set_servo(ServoSetup.LOCK_SERVO_PIN, ServoSetup.LOCK_SERVO_LOCKED)
		self.is_locked = True
    #Defines Unlock
	def unlock(self):
		self.servo.set_servo(ServoSetup.LOCK_SERVO_PIN, config.LOCK_SERVO_UNLOCKED)
		self.is_locked = False

	def is_button_up(self):
		old_state = self.button_state
		self.button_state = RPIO.input(ServoSetup.BUTTON_PIN)
		if old_state == config.BUTTON_DOWN and self.button_state == ServoSetup.BUTTON_UP:
			time.sleep(20.0/1000.0)
			self.button_state = RPIO.input(ServoSetup.BUTTON_PIN)
			if self.button_state == ServoSetup.BUTTON_UP:
				return True
		return False
