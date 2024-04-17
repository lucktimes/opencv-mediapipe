import cv2,mediapipe as mp
import PoseEstimateModule as pm
import numpy as np
cap=cv2.VideoCapture(0)
wCam,hCam=1920,1080
cap.set(3,wCam)
cap.set(4,hCam)
times=0
dirR=0
dirL=0
mpDraw=mp.solutions.drawing_utils
detector=pm.PoseDetector()
kernel=np.zeros((300,500,3),np.uint8)
while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=detector.FindPose(frame,draw=False)
    if len(detector.FindPosition(frame)):
        RightAngle=int(detector.FindAngle(frame,12,14,16))
        LeftAngle=360-int(detector.FindAngle(frame,11,13,15))
        if RightAngle<=35 :
            if dirR==0:
                dirR=1
        if RightAngle>=130 and RightAngle<=180:
            if dirR==1:
                times+=1
                dirR=0
        if LeftAngle<=35 :
            if dirL==0:
                dirL=1
        if LeftAngle>=130 and LeftAngle<=180:
            if dirL==1:
                times+=1
                dirL=0
    per=np.interp(RightAngle,(0,180),(0,300))
    #cv2.rectangle(kernel,(200,50),(250,400),(0,255,0),cv2.FILLED)
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    frame=cv2.flip(frame,1)
    cv2.putText(frame,f'angle:{str(RightAngle),str(LeftAngle)}',(50,70),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),2)
    cv2.imshow('Video',frame)
    
    cv2.putText(kernel,f'times:{times}',(50,70),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)
    cv2.imshow('report',kernel)
    kernel=np.zeros((300,500,3),np.uint8)