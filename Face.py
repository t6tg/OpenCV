import cv2
def draw_boundary():
    
vdo = cv2.VideoCapture("video.mp4")
while(True):
    ret,frame = vdo.read()
    cv2.imshow('frame' , frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
vdo.release()
cv2.destroyAllWindows()
