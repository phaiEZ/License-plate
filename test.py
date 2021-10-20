import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
i = 0
while (True) :
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,68,154])
    upper_red = np.array([180,255,243])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i += 1
    for cnt in contours:
    	area = cv2.contourArea(cnt)
    	approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
    	cv2.drawContours(frame,[cnt],0,(0,0,0),5)
    	if area > 400:
    		if len(approx) == 4:
    			print("x")
    			cv2.imwrite('123.jpg',frame)
    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    if (cv2.waitKey(1) & 0xFF == ord("o")) :
        break

cap.release()
cv2.destroyAllWindows()

