#pose estimate min
import cv2,mediapipe as mp
cap=cv2.VideoCapture(0)

mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils

while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=frame.shape
            cx,cy=int(lm.x*w) ,int(lm.y*h)
            cv2.circle(frame,(cx,cy),5,(255,0,255),cv2.FILLED)
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    frame=cv2.flip(frame,1)
    cv2.imshow('Video',frame)