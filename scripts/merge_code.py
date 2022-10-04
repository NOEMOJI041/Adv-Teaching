import cv2
from __future__ import print_function
import cv2 as cv
import argparse

import RPi.GPIO as GPIO
import time
from simple_facerec import SimpleFacerec
from line import Line_detection


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
servo = GPIO.PWM(27, 50) # GPIO 17 for PWM with 50Hz
servo.start(2.5) # Initialization

min_servo = .1
max_servo = 10.5

servo_position = 5

servo.ChangeDutyCycle(servo_position)

# Encode faces from a folder
sfr = SimpleFacerec()
ld = Line_detection()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        sub = 320 - int((x1 + x2)/2)


        if int((x1 + x2)/2) >320 and servo_position>= .5:
            servo_position = servo_position - .2
            servo.ChangeDutyCycle(servo_position)
            time.sleep(.1)
            print("turn left")
       
        if int((x1 + x2)/2) < 320 and servo_position>= 10:
            servo_position = servo_position + .2
            servo.ChangeDutyCycle(servo_position)
            print("turn right")

        

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        cv2.circle(frame, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (255, 255, 255), -1)
        ld.draw_grid(frame,(2,2))
        cv2.line(frame,(int((x1 + x2) / 2), 0),(int((x1 + x2) / 2), 480), color=(0, 255, 0), thickness=3)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()