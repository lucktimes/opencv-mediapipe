#gesture volume control
import cv2,mediapipe as mp
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap=cv2.VideoCapture(0)

mpDraw=mp.solutions.drawing_utils
wCam,hCam=1920,1080
cap.set(3,wCam)
cap.set(4,hCam)
detector=htm.HandDetecter()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volrange=volume.GetVolumeRange()
minvol=volrange[0]
maxvol=volrange[1]

while True:
    ret,frame=cap.read()
    frame=detector.findHands(frame)
    lmList=detector.findPosition(frame,draw=False)
    if len(lmList)!=0:
        x1,y1=lmList[4][1],lmList[4][2]
        x2,y2=lmList[8][1],lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(frame,(cx,cy),7,(0,255,0),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        vol=np.interp(length,[50,300],[minvol,maxvol])
        volume.SetMasterVolumeLevel(vol, None)
        #print(vol)
    if not ret:
        break
    if cv2.waitKey(1)==ord('q'):
        break
    frame=cv2.flip(frame,1)
    cv2.imshow('Video',frame)