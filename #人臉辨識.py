#人臉辨識
import cv2
img=cv2.VideoCapture(0)
FaceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:   
    ret,frame=img.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    facerect=FaceCascade.detectMultiScale(gray,1.2,5)
    
    for (x,y,w,h) in facerect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('video',frame)
    if cv2.waitKey(2)==ord('q'):
        break

