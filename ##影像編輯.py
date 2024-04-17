##OpenCV
import cv2
import numpy as np
import random
'''
video=cv2.VideoCapture(0)##攝像頭取得畫面   

while True:
    ret,frame=video.read()
    if ret:
        frame=cv2.resize(frame,(700,500))
        cv2.imshow('video',frame)
    else:
        break
    if cv2.waitKey(1)==ord('q'):
        break
'''
#myimg=np.empty((400,400,3), np.uint8)
myimg=cv2.imread('testimg.jpg')
'''for row in range(300):
    for col in range(myimg.shape[1]):
        myimg[row][col]=[random.randint(0,100),random.randint(100,255),random.randint(0,255)]
'''
kernel=np.ones((10,10),np.uint8)#8bit array 3*3
gray=cv2.cvtColor(myimg,cv2.COLOR_BGR2GRAY)#灰階
blur=cv2.GaussianBlur(myimg,(11,11),20)#模糊
canny=cv2.Canny(myimg,150,300)#邊緣
dilate=cv2.dilate(canny,kernel,iterations=3)#膨脹
erode=cv2.erode(dilate,kernel,iterations=2)#輕實
hsv=cv2.cvtColor(myimg,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
cv2.imshow('erode',erode)
cv2.imshow('dilate',dilate)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.waitKey(0)
