import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow('our like image',frame)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()
