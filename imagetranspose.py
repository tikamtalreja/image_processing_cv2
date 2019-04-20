import cv2
import numpy as nu
img = cv2.imread("cat.jpg")
transposed_img = cv2.transpose(img)
cv2.imshow("original",img)
cv2.imshow("transposed_img",transposed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
