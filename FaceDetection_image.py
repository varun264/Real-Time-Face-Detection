import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/mllab/varun/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('/home/mllab/varun/click.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize=(30,30)
        )

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
