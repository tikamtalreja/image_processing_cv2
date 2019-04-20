import cv2

def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edge= cv2.Canny(image_gray_blur,10,100)
    ret,mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    return mask


cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow("our live edge detection",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

