import cv2  
import numpy as np  
img = cv2.imread('/home/rachel/Documents/data/1.jpeg',0)  
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #彩色转灰度  
ret,thresh = cv2.threshold(img,127,255,0)   #二值化  
image,contours,hierarchy = cv2.findContours(thresh, 1, 2)  
cnt = contours[0]   #选取其中的第一个轮廓  
M = cv2.moments(cnt)  #对第一个轮廓  
print (M)             #打印出所有计算的M的参数，其各个数值的计算公式参考http://blog.csdn.net/qq_18343569/article/details/46913501  
cx = int(M['m10']/M['m00'])  #X方向的重心，其中M['m10']表示的是x方向的一阶空间矩，M['m00']表示面积，M['m00']也可以通过cv2.contourArea() 计算得到  
cy = int(M['m01']/M['m00']) #Y方向的重心  
