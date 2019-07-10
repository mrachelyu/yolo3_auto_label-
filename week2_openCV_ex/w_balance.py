
#link:https://gist.github.com/DavidYKay/9dad6c4ab0d8d7dbf3dc#file-simple_cb-py-L46
import cv2
import math
import numpy as np
import sys

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()

def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix

def simplest_cb(img, percent):
    assert img.shape[2] == 3
    assert percent > 0 and percent < 100

    half_percent = percent / 200.0

    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        # find the low and high precentile values (based on the input percentile)
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1

        flat = np.sort(flat)

        n_cols = flat.shape[0]

        low_val  = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil( n_cols * (1.0 - half_percent))]

        print ("Lowval: ", low_val)
        print ("Highval: ", high_val)

        # saturate below the low percentile and above the high percentile
        thresholded = apply_threshold(channel, low_val, high_val)
        # scale the channel
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

if __name__ == '__main__':
    img = cv2.imread(r'/home/rachel/Documents/data/5.jpg')
 
    res = cv2.resize(img,(255,255))
    out = simplest_cb(res, 1)
    cv2.imshow("before", res)
    cv2.imshow("after", out)
    cv2.waitKey(0)

'''
#
import cv2 as cv
# import num py as np
 
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
 
balance_img = cv.merge([b, g, r])

cv.imshow('ps before',img)
cv.imshow('ps after',balance_img)


cv.waitKey(0)
cv.destroyAllWindows()
'''



'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/home/rachel/Documents/data/1.jpeg')
b, g, r = cv2.split(img)
cv2.imshow('ps before', img)
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
cv2.imshow('ps after', img_0)

while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()

'''



import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def draw(img, name):
    plt.title(name)
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
    col = ['b', 'g', 'r']
    j = 0
    for i in [hist_b, hist_g, hist_r]:
        plt.plot(i, color=col[j])
        j += 1
    plt.xlim([0, 256])
    # plt.show()


def detection(img):
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(img_lab)
    d_a, d_b, M_a, M_b = 0, 0, 0, 0
    for i in range(m):
        for j in range(n):
            d_a = d_a + a[i][j]
            d_b = d_b + b[i][j]
    d_a, d_b = (d_a / (m * n)) - 128, (d_b / (n * m)) - 128
    D = np.sqrt((np.square(d_a) + np.square(d_b)))

    for i in range(m):
        for j in range(n):
            M_a = np.abs(a[i][j] - d_a - 128) + M_a
            M_b = np.abs(b[i][j] - d_b - 128) + M_b

    M_a, M_b = M_a / (m * n), M_b / (m * n)
    M = np.sqrt((np.square(M_a) + np.square(M_b)))
    k = D / M
    print('偏色值:%f' % k)
    return


img = cv2.imread('/home/rachel/Documents/data/3.jpeg')
img_gray = cv2.imread('/home/rachel/Documents/data/3.jpeg', 2)
b, g, r = cv2.split(img)
print(img.shape)
m, n = b.shape
cv2.imshow('ps before', img)
detection(img)
plt.subplot(121)
draw(img, 'origin')

I_r, I_g, = 0, 0
I_r_2 = np.zeros(r.shape)
I_b_2 = np.zeros(b.shape)
sum_I_r_2, sum_I_r, sum_I_b_2, sum_I_b, sum_I_g = 0, 0, 0, 0, 0
max_I_r_2, max_I_r, max_I_b_2, max_I_b, max_I_g = int(r[0][0] ** 2), int(r[0][0]), int(b[0][0] ** 2), int(b[0][0]), int(
    g[0][0])
for i in range(m):
    for j in range(n):
        I_r_2[i][j] = int(r[i][j] ** 2)
        I_b_2[i][j] = int(b[i][j] ** 2)
        sum_I_r_2 = I_r_2[i][j] + sum_I_r_2
        sum_I_b_2 = I_b_2[i][j] + sum_I_b_2
        sum_I_g = g[i][j] + sum_I_g
        sum_I_r = r[i][j] + sum_I_r
        sum_I_b = b[i][j] + sum_I_b
        if max_I_r < r[i][j]:
            max_I_r = r[i][j]
        if max_I_r_2 < I_r_2[i][j]:
            max_I_r_2 = I_r_2[i][j]
        if max_I_g < g[i][j]:
            max_I_g = g[i][j]
        if max_I_b_2 < I_b_2[i][j]:
            max_I_b_2 = I_b_2[i][j]
        if max_I_b < b[i][j]:
            max_I_b = b[i][j]

[u_b, v_b] = np.matmul(np.linalg.inv([[sum_I_b_2, sum_I_b], [max_I_b_2, max_I_b]]), [sum_I_g, max_I_g])
[u_r, v_r] = np.matmul(np.linalg.inv([[sum_I_r_2, sum_I_r], [max_I_r_2, max_I_r]]), [sum_I_g, max_I_g])
print(u_b, v_b, u_r, v_r)
b0, g0, r0 = np.zeros(b.shape, np.uint8), np.zeros(g.shape, np.uint8), np.zeros(r.shape, np.uint8)
for i in range(m):
    for j in range(n):
        b0[i][j] = u_b * (b[i][j] ** 2) + v_b * b[i][j]
        g0[i][j] = g[i][j]
        # r0[i][j] = r[i][j]
        r0[i][j] = u_r * (r[i][j] ** 2) + v_r * r[i][j]
img_0 = cv2.merge([b0, g0, r0])

cv2.imshow('ps after', img_0)

detection(img_0)
plt.subplot(122)
draw(img_0, 'fix')
plt.show()
while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()

'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/home/rachel/Documents/data/1.jpeg')
b, g, r = cv2.split(img) #通道分離 (B,G,R)
cv2.imshow('ps before', img)
# detection(img)
m, n, t = img.shape
print(b.shape)
sum = np.zeros(b.shape)
for i in range(m):
    for j in range(n):
        sum[i][j] = int(b[i][j]) + int(g[i][j]) + int(r[i][j])
hists, bins = np.histogram(sum.flatten(), 766, [0, 766])
Y = 765
num, key = 0, 0
while Y >= 0:
    num += hists[Y]
    if num > m * n * 0.01 / 100:
        key = Y
        break
    Y = Y - 1

sum_b, sum_g, sum_r = 0, 0, 0
time = 0
for i in range(m):
    for j in range(n):
        if sum[i][j] >= Y:
            sum_b += b[i][j]
            sum_g += g[i][j]
            sum_r += r[i][j]
            time = time + 1

avg_b = sum_b / time
avg_g = sum_g / time
avg_r = sum_r / time

for i in range(m):
    for j in range(n):
        b[i][j] = b[i][j] * 255 / avg_b
        g[i][j] = g[i][j] * 255 / avg_g
        r[i][j] = r[i][j] * 255 / avg_r
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
cv2.imshow('ps after', img_0)
"""
注释的内容为灰度世界假设算法
"""
# for i in range(m):
#     for j in range(n):
#         if(sum[i][j])
# sum_b, sum_g, sum_r = np.sum(np.ravel(b)), np.sum(np.ravel(g)), np.sum(np.ravel(r))
# avl_b, avl_g, avl_r = sum_b / (m * n), sum_g / (m * n), sum_r / (m * n)
# gray=(avl_b + avl_r + avl_g) / 3
# k_r , k_g , k_b = gray / avl_r , gray / avl_g , gray / avl_b
# for i in range(m):
#     for j in range(n):
#         b[i][j]=b[i][j] * k_b
#         g[i][j]=g[i][j] * k_g
#         r[i][j]=r[i][j] * k_r
# img_0 = cv2.merge([b,g,r])
# cv2.imshow('修图',img_0)

while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()
'''

