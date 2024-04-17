#python畫圖
import numpy as np,cv2

kernel=np.zeros((600,600,3),np.uint8)
#circle=cv2.circle(kernel,(100,100),70,(255,0,0),cv2.FILLED)
text=cv2.putText(kernel,'Hello World!',(0,300),cv2.FONT_HERSHEY_PLAIN,5,(0,200,0))
#kernel=cv2.rectangle(kernel,(100,100),(kernel.shape[1],kernel.shape[0]),(255,0,0),cv2.FILLED) 
cv2.imshow('img',text)

cv2.waitKey(0)



