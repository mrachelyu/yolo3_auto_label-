# !/usr/bin/env python
# -*- coding: UTF-8 -*-

#list：由一串資料組成，有順序且可改變內容的序列
#順序不同就是不同串列

list_a = []                
list_b = list()             
list_c = [1,2.0,"3.0","a"]	#型態不需一致

'''
print("type(list_c):", type(list_c))
print("list_c:", list_c)

# string to list
list_a = list('cat')

print("list_a:", list_a)
# tuple to list

tuple_a = (1, 'a', 3.14)
list_b = list(tuple_a)
print("list_b:", list_b)
'''

list_d = [1,9,9,7,9,5]
list_d.append(0)	#在串列最後面加0

print(list_d)	#a = [1,9,9,7,9,5,0]

list_d = [1,9,9,7,9,5]         
list_d.insert(1,0)	#在1後面加0

print(list_d)	#a = [1,0,9,9,7,9,5]

list_d = [1,9,1,9,7,9,5] 
list_d.remove(1)             #移除坐左邊數過來第一個1

print(list_d)
print("")


#--------------------------------------------------------------------------


a =  [1,9,9,7,9,5]


print(a[1])             #9


print(a[-1])            #5


print(a[0:3])           #[1,9,9]


print(a[5:])            #[5]


print(a[-3:])           #[7,9,5]  從-3往-1


print("")


#--------------------------------------------------------------------------

print(a.index(9))       #1 括號中的數字位置
print(a.count(9))       #3括號中的數字出現次數
print("")



