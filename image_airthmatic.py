import cv2
import numpy as np
img = cv2.imread("cat.jpg")
cv2.imshow("orignal",img)
m = np.ones(img.shape,dtype="uint8")*50

added = cv2.add(img,m)
cv2.imshow("added ",added)
subtract = cv2.subtract(img,m)
cv2.imshow("subtract ",subtract)
multiply = cv2.multiply(img,m)
cv2.imshow("multiply ",multiply)
cv2.waitKey(0)
cv2.destroyAllWindows()