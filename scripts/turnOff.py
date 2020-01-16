import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(7.5)

p.ChangeDutyCycle(12.5)
sleep(1)

p.stop()
GPIO.cleanup()
