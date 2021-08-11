#libraries
import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier('/home/mllab/varun/haarcascades/haarcascade_frontalface_default.xml')
i = 1
faces = []
#accessing raspberry pi cam
dispW = 320
dispH = 240
flip = 0
picam = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(picam)

while True:
    ret, frame = cam.read()
    save = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for i in range(len(face)):
        faces.append(face)
    for (x,y,w,h) in face:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        saved = save[y:y+h,x:x+w]
        stri = 'face'+str(i)+'.jpg'
        #the detected face is saved facei.jpg
        cv2.imwrite(stri,saved)
        i=i+1
    cv2.imshow('cam',frame)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cam.release()
cv2.destroyAllWindows()
