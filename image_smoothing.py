import cv2
import numpy as np

img = cv2.imread("cat.jpg")
cv2.imshow("orignal ",img)
cv2.imshow("blurred",cv2.blur(img,(3,3)))
cv2.waitKey(0)

cv2.imshow("Gussian blurred",cv2.GaussianBlur(img,(3,3),0))
cv2.waitKey(0)

cv2.imshow("Median blurred",cv2.medianBlur(img,3))
cv2.waitKey(0)

cv2.imshow("bilateral blurred",cv2.bilateralFilter(img,9,75,75))
cv2.waitKey(0)
cv2.destroyAllWindows()
