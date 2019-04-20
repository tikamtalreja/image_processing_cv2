import cv2
import numpy as nu
img = cv2.imread("cat.jpg")
smaller = cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow("smaller",smaller)
cv2.imshow("bigger",larger)
cv2.waitKey(0)
cv2.destroyAllWindows()