# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:58:54 2023

@author: MONSTER
"""

import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

start_time = time.time()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if(len(faces)==1):
        start_time=time.time()
    
    if len(faces) == 0 and time.time() - start_time > 3:
        print('3 saniyedir yüz tespiti yapılamıyor!')
        start_time=time.time()
        continue
    if (len(faces)>=2):
        img_name = "screenshot.jpg"
        cv2.imwrite(img_name, frame)
        print("Ekran görüntüsü kaydedildi.")
        time.sleep(1)
        continue
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
