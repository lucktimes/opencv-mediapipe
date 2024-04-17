#pose estimate min
import cv2,mediapipe as mp
import math

class PoseDetector():

    def __init__(self,mode=False,UpBody=False,smooth=True):
        self.mode=mode
        self.UpBody=UpBody
        self.smooth=smooth
        #self.detectionCon=detectionCon
        #self.trackCon=trackCon

        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(self.mode,self.UpBody,self.smooth)
        self.mpDraw=mp.solutions.drawing_utils

    def FindPose(self,frame,draw=True):
        imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(frame,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return frame
    def FindPosition(self,frame,draw=True):
        self.lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                    h,w,c=frame.shape
                    cx,cy=int(lm.x*w) ,int(lm.y*h)
                    self.lmList.append([id,cx,cy])
            if draw:
                cv2.circle(frame,(cx,cy),5,(255,0,255),cv2.FILLED)
        return self.lmList
    def FindAngle(self,frame,p1,p2,p3,draw=True):
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]

        angle=math.degrees(math.atan2(y1-y2,x1-x2)-math.atan2(y3-y2,x3-x2))
        if angle<0:
            angle+=360
        if draw:
            cv2.circle(frame,(x1,y1),7,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x1,y1),10,(0,0,255),2)
            cv2.circle(frame,(x2,y2),7,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),10,(0,0,255),2)
            cv2.circle(frame,(x3,y3),7,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x3,y3),10,(0,0,255),2)
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.line(frame,(x3,y3),(x2,y2),(255,0,255),3)
            
        return angle


def main():
    cap=cv2.VideoCapture(0)
    detector=PoseDetector()
    
    while True:
        ret,frame=cap.read()
        detector.FindPose(frame)
        lmList=detector.FindPosition(frame)
        print(lmList)
        if not ret:
            break
        if cv2.waitKey(1)==ord('q'):
            break
        frame=cv2.flip(frame,1)
        cv2.imshow('Video',frame)

if __name__=='__main__':
    main()