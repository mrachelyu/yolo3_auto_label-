# !/usr/bin/env python
# -*- coding: UTF-8 -*-

#list：由一串資料組成，有順序且可改變內容的序列
#順序不同就是不同串列

list_a = []                
list_b = list()             
list_c = [1,2.0,"3.0","a"] #型態不需一致


print("type(list_c):", type(list_c))
print("list_c:", list_c)

# string to list
list_a = list('cat')

print("list_a:", list_a)
# tuple to list

tuple_a = (1, 'a', 3.14)
list_b = list(tuple_a)
print("list_b:", list_b)
