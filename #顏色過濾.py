#顏色過濾
def empty(k):
    pass
import cv2,numpy as np
img=cv2.imread('img2.png')
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,320)

cv2.createTrackbar('HueMin','TrackBar',0,179,empty)
cv2.createTrackbar('HueMax','TrackBar',179,179,empty)
cv2.createTrackbar('SatMin','TrackBar',0,255,empty)
cv2.createTrackbar('SatMax','TrackBar',255,255,empty)
cv2.createTrackbar('ValMin','TrackBar',0,255,empty)
cv2.createTrackbar('ValMax','TrackBar',255,255,empty)

while True:
    HueMin=cv2.getTrackbarPos('HueMin','TrackBar')
    HueMax=cv2.getTrackbarPos('HueMax','TrackBar')
    SatMin=cv2.getTrackbarPos('SatMin','TrackBar')
    SatMax=cv2.getTrackbarPos('SatMax','TrackBar')
    ValMin=cv2.getTrackbarPos('ValMin','TrackBar')
    ValMax=cv2.getTrackbarPos('ValMax','TrackBar')
    
    lower=np.array([HueMin,SatMin,ValMin])
    upper=np.array([HueMax,SatMax,ValMax])
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('result',result)
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.waitKey(1)
