import sys
import numpy as np
from cv2 import cv2 as cv

haar_face = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
haar_eyes = cv.CascadeClassifier("haarcascade_eye.xml")

video_capture = cv.VideoCapture(0)

if not video_capture.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    deteced_faces = haar_face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in deteced_faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        eye_color = frame[y:y+h, x:x+w]
        eye_gray = gray[y:y+h, x:x+w]
        deteced_eye = haar_eyes.detectMultiScale(
            eye_gray,
            scaleFactor=1.1,
            minNeighbors=5
        )
        for (ex, ey, ew, eh) in deteced_eye:
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
