import cv2
import numpy as np
img = cv2.imread('cat.jpg')
height,width = img.shape[:2]
quator_height,quator_width = height/4,width/4
print(quator_height)
print(quator_width)
T = np.float32([[1,0,quator_width],[0,1,quator_height]])
img_translation = cv2.warpAffine(img,T,(width,height))
cv2.imshow("output1",img)
cv2.imshow("output2",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()