#FingerCounter
import cv2,mediapipe as mp
import os
import HandTrackingModule as htm
cap=cv2.VideoCapture(0)
wCam,hCam=1920,1080
cap.set(3,wCam)
cap.set(4,hCam)
Gesture=[]
TotalFinger=0
TipTDs=[4,8,12,16,20]#tips id
myList=os.listdir('C:/Users/Acer/Desktop/opencv/number')
for imPath in myList:
    img=cv2.imread(f'number/{imPath}')
    img=cv2.resize(img,(200,200))
    Gesture.append(img)
    
detector=htm.HandDetecter()
while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=detector.findHands(frame)
    lmList=detector.findPosition(frame,draw=False)
    finger=[]
    if len(lmList)!=0:
        if lmList[TipTDs[0]][1]<lmList[TipTDs[0]-1][1]:#Thumb
            finger.append(0)
        else:
            finger.append(1)
        for ids in range(1,5):#else 4 finger
            if lmList[TipTDs[ids]][2]<lmList[TipTDs[ids]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        TotalFinger=finger.count(1)
        

    frame=cv2.flip(frame,1)
    frame[0:200,0:200]=Gesture[TotalFinger]
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    
    cv2.imshow('Video',frame)