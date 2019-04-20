import cv2
#reading the image from te same dir where the project is and at a same time changing it to grayscale.
img  = cv2.imread("cat.jpg",0)
#showing the  output  with an output window name output and passing the img
cv2.imshow("output",img)
#use to wait till any interruot is given through key
cv2.waitKey(0)
#this statement will create a new image with format of png
cv2.imwrite("qwerty.png",img)
#crerate a black white inage and will chnge the rbg value from 127 to 255 in 1 and rest in 0
ret,bw = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow("blackWhite",bw)
cv2.waitKey(0)

#hue image of a picture

# img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv channel',img_HSV)


#destroy all the windows bedore exiting from the program
cv2.destroyAllWindows()
