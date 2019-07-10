import cv2
import numpy as np

img = cv2.imread('/home/rachel/Documents/data/1.jpeg')
type(img)
img.shape

cv2.imshow('my photo',img)

cv2.waitKey(0)
cv2.destroyWindow(1)
