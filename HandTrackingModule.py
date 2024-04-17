#Hand Tracking Module
import cv2, time
import mediapipe as mp
import math


class HandDetecter():
    def __init__(self,mode=False,maxHands=2):
        self.mode=mode
        self.maxHands=maxHands
        #self.detectionCon=detectionCon
        #self.trackCon=trackCon
        
        self.mpHands=mp.solutions.hands
        self.hand=self.mpHands.Hands()
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self,frame,draw=True): 
        imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.result=self.hand.process(imgRGB)
            
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame,handLms,self.mpHands.HAND_CONNECTIONS)   
        return frame
    
    def findPosition(self,frame,handNo=0,draw=True):
        xlist=[]
        ylist=[]
        self.lmList=[]
        box=[]
        self.results=self.hand.process(frame)
        if self.results.multi_hand_landmarks:
            self.myHand=self.results.multi_hand_landmarks[handNo]
            for id ,lm in enumerate(self.myHand.landmark):
                h, w, c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                xlist.append(cx)
                ylist.append(cy)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(frame,(cx,cy),10,(0,255,255),cv2.FILLED)
            xmin,xmax=min(xlist),max(xlist)
            ymin,ymax=min(ylist),max(ylist)
            box=xmin,ymin,xmax,ymax
        return self.lmList,box
    
    def fingersUp(self):
        fingers=[]
        self.tipIDs=[4,8,12,16,20]
        #Thumb
        if self.lmList[self.tipIDs[0]][1]>self.lmList[self.tipIDs[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #else fingers
        for id in range(1,5):
            if self.lmList[self.tipIDs[id]][2]<self.lmList[self.tipIDs[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    
    def findDistance(self,p1,p2,frame,draw=True,r=15,thin=3):
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        if draw:
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),thin)
            cv2.circle(frame,(x1,y1),r,(255,0,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),r,(255,0,255),cv2.FILLED)
            cv2.circle(frame,(cx,cy),r,(0,0,255),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        return length,frame,[x1,x2,y1,y2,cx,cy]
        
def main():
    cap=cv2.VideoCapture(0)
    pTime=0
    cTime=0 
    detecter=HandDetecter()
    while True:
        ret,frame=cap.read()
        frame=detecter.findHands(frame)
        lmList,box=detecter.findPosition(frame)
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

if __name__ =='__main__':
    main()