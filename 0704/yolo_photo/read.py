# encoding: utf-8
import datetime 
import cv2
import time 
import argparse
import numpy as np
import os

def pic_resize(img,i):
    _x, _y = img.shape[0:2]
    _x = int(_x/i)
    _y = int(_y/i)
    return cv2.resize(img, (_y, _x))

img = cv2.imread("yolo_photo_0.jpg")
img = pic_resize(img,4)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()