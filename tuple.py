# !/usr/bin/env python
# -*- coding: UTF-8 -*-

#tuple序對：由一連串資料所組成，有順序且不可改變內容的序
# tuple不一定要用小括弧

tuple_a = []                 
tuple_b = tuple()             
tuple_c = 1, 2.0, "3.0"
tuple_d = (1, 2.0, "3.0")

print("type(tuple_c):", type(tuple_c))
print("tuple_c:", tuple_c)
print("type(tuple_d):", type(tuple_d))
print("tuple_d:", tuple_d)

# string to tuple
tuple_a = tuple('cat')
print("tuple_a:", tuple_a)

# 若元組只有1個元素，在元素後須逗號
tuple_e = (12,) 
print("tuple_e:", tuple_e)
