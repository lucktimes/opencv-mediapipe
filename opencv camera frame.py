#opencv camera frame
import cv2,mediapipe as mp
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