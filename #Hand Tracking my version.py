#Hand Tracking Basics
import cv2, time
import mediapipe as mp
import numpy as np
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hand=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

kernel=np.zeros((1,1,3),np.uint8)

while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hand.process(imgRGB)
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c=frame.shape

                cx, cy=int(lm.x*w),int(lm.y*h)
                
                cv2.circle(frame,(cx,cy),10,(255,0,255),cv2.FILLED)
                cv2.circle(kernel,(cx,cy),7,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            mpDraw.draw_landmarks(kernel,handLms,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    if ret:
        frame = cv2.flip(frame, 1)
        kernel= cv2.flip(kernel, 1)
        #cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        
        cv2.resize(frame,(1920,1080))
        
        cv2.imshow('video',frame)
        cv2.imshow('black',kernel)
        kernel=np.zeros(frame.shape,np.uint8)
    if cv2.waitKey(1)==ord('q'):
        break


