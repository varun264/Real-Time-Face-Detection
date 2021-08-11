import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('/home/mllab/varun/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('/home/mllab/varun/videoplayback.avi')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in face:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('cam',frame)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
