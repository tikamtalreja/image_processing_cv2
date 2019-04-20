import cv2
import numpy as np

img = cv2.imread('cat.jpg')
kernel_sharp = np.array([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,25,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],])
sharaped = cv2.filter2D(img,-1,kernel_sharp)
cv2.imshow('original',img)
cv2.imshow('sharaped',sharaped)
cv2.waitKey(0)
cv2.destroyAllWindows()
