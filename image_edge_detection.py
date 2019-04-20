import cv2
import numpy as np

img = cv2.imread("cat3.jpg",0)
height,width = img.shape

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("original",img)
cv2.imshow("lapascian",laplacian)
cv2.waitKey(0)
#best sutited or edg detection 
canny = cv2.Canny(img,20,200)
cv2.imshow("canny",canny)
cv2.waitKey(0)
