import cv2
img = cv2.imread("Lion.jpg" , -1)
img = cv2.circle(img , (384,255) ,50 , (0,255,0) , 10)
img = cv2.putText(img , "OpenCV" , (10,100) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.imshow('Show Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

