import cv2,mediapipe as mp
import numpy as np
import os
import HandTrackingModule as htm
folderPath=''#picture path
myList=os.listdir(folderPath)
pen=[]
for imPath in myList:
    img=cv2.imread(f'number/{imPath}')
    pen.append(img)

cap=cv2.VideoCapture(0)
mpDraw=mp.solutions.drawing_utils

while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    frame=cv2.flip(frame,1)
    cv2.imshow('Video',frame)