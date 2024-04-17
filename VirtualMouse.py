#opencv camera frame
import cv2,mediapipe as mp
import HandTrackingModule as htm
import numpy as np
import pyautogui
import ctypes
cap=cv2.VideoCapture(0)
wCam,hCam=1080,720
cap.set(3,wCam)
cap.set(4,hCam)
detector=htm.HandDetecter(maxHands=1)
mpDraw=mp.solutions.drawing_utils
user32 = ctypes.windll.user32
finger=[0,0,0,0,0]
wScr,hScr=user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)
while True:
    ret,frame=cap.read()
    frame=detector.findHands(frame,draw=False)
    lmList,box=detector.findPosition(frame,draw=False)
    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:] 
        finger=detector.fingersUp()
    else:
        finger=[0,0,0,0,0]
    #print(finger)
    if finger[1]==1 and finger[3]==0:
        x3=np.interp(x1,(0,wCam),(0,wScr))
        y3=np.interp(y1,(0,hCam),(0,hScr))
        pyautogui.moveTo(int(wScr-x3),int(y3),duration=0.2)
        #cv2.circle(frame,(x1,y1),15,(255,0,255),cv2.FILLED)
    if finger[0]==1:
        pyautogui.click()
    if finger[2]==1:
        pyautogui.doubleClick()
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    #frame=cv2.flip(frame,1)
    #cv2.imshow('Video',frame)