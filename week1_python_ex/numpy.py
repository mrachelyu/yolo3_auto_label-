
'''
numpy陣列
	Numpy 的重點在於陣列的操作，其所有功能特色都建築在同質且多重維度的 ndarray（N-dimensional array）上。ndarray 的關鍵屬性是維度（ndim）、形狀（shape）和數值類型（dtype）。 一般我們稱一維陣列為 vector 而二維陣列為 matrix。一開始我們會引入 numpy 模組，透過傳入 list 到 numpy.array() 創建陣列。

'''

# -*- coding: utf-8 -*-

import numpy;

print('used list to creat 1-D')
data = [1,2,3,4,5,6]
x = numpy.array(data)
print(x) 
print(x.dtype) 

print('used list to creat 2-D')
data = [[1,2],[3,4],[5,6]]
x = numpy.array(data)
print(x) 
print(x.ndim) 
print(x.shape) 

print('使用zero/ones/empty创建数组:根据shape来创建')
x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
print(x)
x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
print(x)
x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
print(x)
x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
print(x)

print('使用arrange生成连续元素')
print(numpy.arange(6)) 	   # [0,1,2,3,4,5,] 
print(numpy.arange(0,6,2)) # [0, 2，4]





