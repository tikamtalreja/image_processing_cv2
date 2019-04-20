import cv2
import numpy as np

img = cv2.imread("cat.jpg")
cv2.imshow("orignal ",img)
kernel_3x3 = np.ones((3,3),np.float32)/9
blurred = cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow("blurred 1",blurred)

kernel_5x5 = np.ones((5,5),np.float32)/25
blurred2 = cv2.filter2D(img,-1,kernel_5x5)
cv2.imshow("blurred 2",blurred2)

kernel_7x7 = np.ones((7,7),np.float32)/49
blurred3 = cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow("blurred 3",blurred3)
cv2.waitKey(0)
cv2.destroyAllWindows()
