# encoding: utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os

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

#自訂閾值+開運算
def pic_pro(img,thresh):
    _clone = img.copy()
    _ret,_thresh1 = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
    _kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    _opened = cv2.morphologyEx(_thresh1, cv2.MORPH_OPEN, _kernel)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if(_opened[x,y] == 0):
                img[x,y] = 0

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

# if __name__ == "__main__":

orginpath = "./orgin"
datapath = "./data"
if os.path.isdir(orginpath)==False:
    os.makedirs(orginpath)
if os.path.isdir(datapath)==False:
    os.makedirs(datapath)
    
cv2.namedWindow("camera")
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)

num = 0
n = 0
c = 0

orginfolder = "%s/%s" % (orginpath,c)
datafolder = "%s/%s" % (datapath,c)
if os.path.isdir(orginfolder)==False:
    os.makedirs(orginfolder)
if os.path.isdir(datafolder)==False:
    os.makedirs(datafolder)

k = 0
s = -1
c = 0

threshod = 40
thresh = 40

while True:
    
    _,img = capture.read()
    cv2.imshow("camera",img)

    key = cv2.waitKey(10)

    img_fin = np.zeros(img.shape,np.uint8)

    if key == 27:
        print("end")
        break

    elif key == ord('b'):
        num = 0
        s = s + 1
        orginfolder = "%s/%s" % (orginpath,c)
        filename = "%s-%s.jpg" % (s,num)
        cv2.imwrite(orginfolder+'/'+filename,img)
        num = 1
        print("儲存背景")

    elif key == ord('n'):
        num = 0
        c = c + 1
        orginfolder = "%s/%s" % (orginpath,c)
        os.makedirs(orginfolder)
        datafolder = "%s/%s" % (datapath,c)
        os.makedirs(datafolder)
        print("下一元件")
        
    elif key == ord(' '):
        orginfolder = "%s/%s" % (orginpath,c)
        filename = "%s-%s.jpg" % (s,num)
        cv2.imwrite(orginfolder+'/'+filename,img)
        print("儲存原圖")
        
        img_b = cv2.imread(orginfolder+'/'+str(s)+'-'+str(k)+'.jpg')
        img = cv2.imread(orginfolder+'/'+str(s)+'-'+str(num)+'.jpg')
        print("讀取原圖和背景")
        gray_b = cv2.cvtColor(img_b,cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_clone = gray.copy()
        img_fin = img.copy()
        pic_sub(gray_b,gray,img_clone,threshod)
        print("背景消去")
        pic_autoth(img_clone)
        print("自適應閾值")
        pic_op(img_clone)
        print("開運算")
        pic_fin(img_fin,img_clone)
        print("切割原圖")
        cv2.imshow("1",img_fin)
        cv2.imshow("clone",img_clone)

        x,y,w,h=cv2.boundingRect(img_clone)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        print("取邊界")

        datafolder = "%s/%s" % (datapath,c)
        listname="list.txt"
        f = open(listname,'a')
        f.writelines('orgin/%d/%d-%d.jpg %d,%d,%d,%d\n'% (c,s,num,x,y,x+w,y+h))
        f.close()
        print("寫入list")
        cv2.imshow("fin",img)
        cv2.imwrite(datafolder+'/'+filename,img)
        print("儲存結果")
        num = num + 1

cv2.waitKey(0)
cv2.destroyAllWindows()
