#test
import cv2, time
import mediapipe as mp
import HandTrackingModule as htm

cap=cv2.VideoCapture(0)
pTime=0
cTime=0 
detecter=htm.HandDetecter()
while True:
    ret,frame=cap.read()
    frame=detecter.findHands(frame)
    lmList=detecter.findPosition(frame,draw=False)
    if len(lmList)!=0:
        print(lmList[4])
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    if ret:
        frame = cv2.flip(frame, 1)
        cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        cv2.resize(frame,(0,0),fx=1.5,fy=1.5)
        cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break