import cv2

import time

c=1
if __name__ == '__main__':

    cv2.namedWindow("camera")
    capture = cv2.VideoCapture(0)
    #capture = cv2.CaptureFromFile("Video.avi")
 
    num = 0
    while True:
        _,img = capture.read()
        cv2.imshow("camera",img)

        key = cv2.waitKey(10)
        if key == 27:
            break
        if key == ord(' '):
            num = num+1
            filename = "frmaes_%s.jpg" % num
            cv2.imwrite('img_5/'+str(c) + '.jpg',img)
            c=c+1


    del(capture)
cv2.destroyAllWindows()