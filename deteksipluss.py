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

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 109, 250])
upper_red = np.array([22, 167, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel)
mask = cv2.dilate(mask, kernel, iterations = 3)

# Contours detection
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    approx = cv2.approxPolyDP(cnt, 0.05*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        gerak()
