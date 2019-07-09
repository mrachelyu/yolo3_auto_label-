import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/home/rachel/Documents/data/1.jpeg')
b, g, r = cv2.split(img)
cv2.imshow('origin', img)
"""
YUV空间
"""
def con_num(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0

yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
(y, u, v) = cv2.split(yuv_img)
# y, u, v = cv2.split(img)
m, n = y.shape
sum_u, sum_v = 0, 0
max_y = np.max(y.flatten())
print(max_y)
for i in range(m):
    for j in range(n):
        sum_u = sum_u + u[i][j]
        sum_v = sum_v + v[i][j]

avl_u = sum_u / (m * n)
avl_v = sum_v / (m * n)
du, dv = 0, 0
print(avl_u,avl_v)
for i in range(m):
    for j in range(n):
        du = du + np.abs(u[i][j] - avl_u)
        dv = dv + np.abs(v[i][j] - avl_v)

avl_du = du / (m * n)
avl_dv = dv / (m * n)
num_y, yhistogram, ysum = np.zeros(y.shape), np.zeros(256), 0
for i in range(m):
    for j in range(n):
        value = 0
        if np.abs(u[i][j] - (avl_u + avl_du * con_num(avl_u))) < 0.5 * avl_du or np.abs(
                v[i][j] - (avl_v + avl_dv * con_num(avl_v))) < 0.5 * avl_dv:
            value = 1
        else:
            value = 0

        if value <= 0:
            continue
        num_y[i][j] = y[i][j]
        yhistogram[int(num_y[i][j])] = 1 + yhistogram[int(num_y[i][j])]
        ysum += 1
print(yhistogram.shape)
sum_yhistogram = 0
# hists2, bins = np.histogram(yhistogram, 256, [0, 256])
# print(hists2)
Y = 255
num, key = 0, 0
while Y >= 0:
    num += yhistogram[Y]
    if num > 0.1 * ysum:
        key = Y
        break
    Y = Y-1
print(key)
sum_r, sum_g, sum_b, num_rgb = 0, 0, 0, 0
for i in range(m):
    for j in range(n):
        if num_y[i][j] > key:
            sum_r = sum_r + r[i][j]
            sum_g = sum_g + g[i][j]
            sum_b = sum_b + b[i][j]
            num_rgb += 1

avl_r = sum_r / num_rgb
avl_g = sum_b / num_rgb
avl_b = sum_b / num_rgb

for i in range(m):
    for j in range(n):
        b[i][j] = int(b[i][j]) * max_y / avl_b
        g[i][j] = int(g[i][j]) * max_y / avl_g
        r[i][j] = int(r[i][j]) * max_y / avl_r
        if b[i][j] > 255:
            b[i][j] = 255
        if b[i][j] < 0:
            b[i][j] = 0
        if g[i][j] > 255:
            g[i][j] = 255
        if g[i][j] < 0:
            g[i][j] = 0
        if r[i][j] > 255:
            r[i][j] = 255
        if r[i][j] < 0:
            r[i][j] = 0

img_0 = cv2.merge([b, g, r])
cv2.imshow('PS_after', img_0)

while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()


'''
import cv2 as cv
import numpy as np
 
# 读取图像
img = cv.imread(r'/home/rachel/Documents/data/1.jpeg')
r, g, b = cv.split(img)
r_avg = cv.mean(r)[0]
g_avg = cv.mean(g)[0]
b_avg = cv.mean(b)[0]
 
# 求各个通道所占增益
k = (r_avg + g_avg + b_avg) / 3
kr = k / r_avg
kg = k / g_avg
kb = k / b_avg
 
r = cv.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
g = cv.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
b = cv.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
 
balance_img = cv.merge([b, g, r]
'''
