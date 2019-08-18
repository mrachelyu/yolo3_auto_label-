# encoding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from pathlib import Path

#遮罩
def pic_mask(img):
    for x in range(0,img.shape[0]):
        for y in range(0,img.shape[1]):
            if (x<img.shape[0]*28/100) or (x>img.shape[0]*65/100):
                img[x,y] = [0,0,0]
            else:
                if (y<img.shape[1]*38/100) or (y>img.shape[1]*65/100):
                    img[x,y] = [0,0,0]

#遮罩v2
def pic_mask_v2(img,A,B,C):
    p0x = A[0]
    p0y = A[1]
    p1x = B[0]
    p1y = B[1]
    p2x = C[0]
    p2y = C[1]
    for px in range(0,img.shape[0]):
        for py in range(0,img.shape[1]):
            Area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
            u = 1/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
            v = 1/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
            if (u>0 and v>0 and u+v<1):
                img[px,py] = img[px,py]
            else:
                img[px,py] = [0,0,0]

#灰階
def pic_gray(img):
    _emptyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    for x in range(0,_emptyimg.shape[0]):
        for y in range(0,_emptyimg.shape[1]):
            B = img[x,y,0]
            G = img[x,y,1]
            R = img[x,y,2]
            _emptyimg[x,y] = B*0.25+G*0.5+R*0.25
    return _emptyimg

#背景消去
def pic_sub(s1,s2,img,threshod):
    _emptyimg = np.zeros(img.shape,np.uint8)
    for x in range(0,_emptyimg.shape[0]):
        for y in range(0,_emptyimg.shape[1]):
            if(s2[x,y] > s1[x,y]):
                _emptyimg[x,y] = s2[x,y] - s1[x,y]
            else:
                _emptyimg[x,y] = s1[x,y] - s2[x,y]

            if(_emptyimg[x,y] < threshod):
                img[x,y] = 0
            else:
                img[x,y] = s2[x,y]

#背景消去_v2
def pic_sub_v2(s1,s2,img,threshod):
    _emptyimg =(img.shape,np.uint8)
    _sub = np.uint8(np.abs(np.int32(s2) - np.int32(s1)))
    for x in range(0,_emptyimg.shape[0]):
        for y in range(0,_emptyimg.shape[1]):
            if(_sub[x,y] < threshod):
                img[x,y] = 0
            else:
                img[x,y] = s2[x,y]

#背景消去BGR
def pic_sub_bgr(s1,s2,img,threshod):
    _emptyimg = img.copy()
    for x in range(0,_emptyimg.shape[0]):
        for y in range(0,_emptyimg.shape[1]):
            b1 = s1[x,y,0]
            g1 = s1[x,y,1]
            r1 = s1[x,y,2]
            b2 = s2[x,y,0]
            g2 = s2[x,y,1]
            r2 = s2[x,y,2]
            if(b1 > b2):
                _emptyimg[x,y,0] = s1[x,y,0] - s2[x,y,0]
            else:
                _emptyimg[x,y,0] = s2[x,y,0] - s1[x,y,0]
            if(g1 > g2):
                _emptyimg[x,y,1] = s1[x,y,1] - s2[x,y,1]
            else:
                _emptyimg[x,y,1] = s2[x,y,1] - s1[x,y,1]
            if(r1 > r2):
                _emptyimg[x,y,2] = s1[x,y,2] - s2[x,y,2]
            else:
                _emptyimg[x,y,2] = s2[x,y,2] - s1[x,y,2]

            if(_emptyimg[x,y,0]<threshod or _emptyimg[x,y,1]<threshod or _emptyimg[x,y,2]<threshod):
                img[x,y] = 0
            else:
                img[x,y] = s2[x,y]

#自適應閾值
def pic_autoth(img):
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#開運算
def pic_op(img):
    _clone = img.copy()
    _kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    _opened = cv2.morphologyEx(_clone, cv2.MORPH_OPEN, _kernel)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if(_opened[x,y] == 0):
                img[x,y] = 0

#切割原圖
def pic_fin(img,emp):
    for x in range(emp.shape[0]):
        for y in range(emp.shape[1]):
            if(emp[x,y] != 0):
                img[x,y] = img[x,y]
                emp[x,y] = 255
            else:
                img[x,y] = (0,0,0)
                emp[x,y] = 0

#找邊界
def pic_xy(self,img,x_max,y_max,x_min,y_min):
    x,y,w,h=cv2.boundingRect(img)
    x_max=x
    y_max=y
    x_min=x+w
    y_min=y+h

#重設大小
def pic_resize(img,i):
    _x, _y = img.shape[0:2]
    _x = int(_x/i)
    _y = int(_y/i)
    return cv2.resize(img, (_y, _x))

# if __name__ == "__main__":

datapath = "./yolo_photo"

num = 1
n = 0
c = 0
k = 0

testfolder = "%s/test_v3" % (datapath) # 
if os.path.isdir(testfolder)==False:
    os.makedirs(testfolder)

threshod = 10
img = cv2.imread(datapath+'/yolo_photo_'+str(num)+'.jpg')
cv2.namedWindow("img")

while True:
    key = cv2.waitKey(10)

    img_b = cv2.imread(datapath+'/yolo_photo_'+str(k)+'.jpg')
    img = cv2.imread(datapath+'/yolo_photo_'+str(num)+'.jpg')
    img_b = pic_resize(img_b,4)
    img = pic_resize(img,4)
    img_fin = np.zeros(img.shape,np.uint8)
    print("讀取原圖和背景")
    A = [95,122]
    B = [310,251]
    C = [92,377]
    pic_mask_v2(img_b,A,B,C)
    pic_mask_v2(img,A,B,C)
    cv2.imshow("Mask_b",img_b)
    cv2.imshow("Mask",img)
    print("加入遮罩")
    gray_b = pic_gray(img_b)
    gray = pic_gray(img)
    cv2.imshow("gray",gray)
    img_clone = gray.copy()
    #img_clone = img.copy()
    img_fin = img.copy()
    pic_sub_v2(gray_b,gray,img_clone,threshod)
    #pic_sub_bgr(img_b,img,img_clone,threshod)
    cv2.imshow("Background_sub",img_clone)
    #img_clone = pic_gray(img_clone)
    print("背景消去")
    pic_autoth(img_clone)
    cv2.imshow("Adaptive_threshold",img_clone)
    print("自適應閾值")
    pic_op(img_clone)
    cv2.imshow("Morph_Open",img_clone)
    print("開運算")
    pic_fin(img_fin,img_clone)
    print("切割原圖")
    cv2.imshow("Cutting",img_fin)
    cv2.imshow("Cutting(Binarization)",img_clone)

    x,y,w,h=cv2.boundingRect(img_clone)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print("取邊界")

    cv2.imshow("fin",img)
    filename = "test_%s.jpg" % (num)
    cv2.imwrite(testfolder+'/'+filename,img)
    print("儲存結果")
    num = num + 1

cv2.waitKey(0)
cv2.destroyAllWindows()
