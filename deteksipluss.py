import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

def gerak():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)

    servo1.start(0)

    servo1.ChangeDutyCycle(2)
    time.sleep(5)

    servo1.ChangeDutyCycle(7)
    time.sleep(2)

    servo1.ChangeDutyCycle(12)
    time.sleep(1)

    servo1.ChangeDutyCycle(2)
    time.sleep(1)

    servo1.stop()
    GPIO.cleanup()

img = cv2.imread('/home/ubuntu/ip/data/foto1.jpg')
