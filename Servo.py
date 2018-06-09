from RPIO import PWM
import ServoSetup

servo = PWM.Servo()
#Program for calibrating servo
print 'Servo Calibration'
print 'Values range from 1000 to 2000 (in microseconds)'
print 'Press Ctrl-C to quit'
print 

while True:
	val = raw_input('Enter servo pulsewidth (1000 to 2000):')
	try:
		val = int(val)
	except ValueError:
		print 'Invalid value, must be between 1000 and 2000'
		continue
	if val < 1000 or val > 2000:
		print 'Invalid value, must be between 1000 and 2000'
		continue
	servo.set_servo(ServoSetup.LOCK_SERVO_PIN, val)
