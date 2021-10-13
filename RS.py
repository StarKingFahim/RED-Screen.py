import cv2
import numpy as np
 
video = cv2.VideoCapture(0) 
image = cv2.imread("bg.jpg")  

cap=cv2.VideoCapture(0)
 
while True:
 
    ret, frame = video.read() 
	
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
 
 
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
 
    mask = cv2.inRange(frame,lower_red,upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
 
    f = frame - res
    f = np.where(f == 0, image, f)
 
    cv2.imshow("video", frame)
    cv2.imshow("Red Screen", f)
 
    if cv2.waitKey(1) == ord('q'):
        break
 
video.release()
cv2.destroyAllWindows()