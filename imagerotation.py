import cv2
import numpy as np
img = cv2.imread('cat.jpg')
#extracting the width and height f a image
height,width = img.shape[:2]
rotation_matrix1 = cv2.getRotationMatrix2D((width/2,height/2),60,.5)
rotation_matrix2 = cv2.getRotationMatrix2D((width/2,height/2),60,.8)
rotation_matrix3 = cv2.getRotationMatrix2D((width/2,height/2),60,.3)
rotated_matrix = cv2.warpAffine(img,rotation_matrix1,(width,height))
rotated_matrix2 = cv2.warpAffine(img,rotation_matrix2,(width,height))

rotated_matrix3= cv2.warpAffine(img,rotation_matrix3,(width,height))

cv2.imshow("normal", img)
cv2.imshow("rotated",rotated_matrix)
cv2.imshow("rotated234",rotated_matrix2)
cv2.imshow("rotated23",rotated_matrix3)
cv2.waitKey(0)
cv2.destroyAllWindows()