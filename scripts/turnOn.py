import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(2.5)

try:
    while True:
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.stop()
        GPIO.cleanup()
