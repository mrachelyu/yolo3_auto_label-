# !/usr/bin/env python
# -*- coding: UTF-8 -*-

#list：由一串資料組成，有順序且可改變內容的序列
#順序不同就是不同串列

list_a = []                
list_b = list()             
list_c = [1,2.0,"3.0","a"] #型態不需一致

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
list_d.append(0,1)             #append a number 0
print(list_d)                       #a = [1,1,4,5,1,4,0]

list_d = [1,9,9,7,9,5]         
list_d.insert(1,0)           #append a number 0 after 1


print(list_d)               	     #a = [1,0,1,4,5,1,4]







list_d = [1,1,4,5,1,4]


list_d.remove(1)             #remove 1


print(list_d)


print("")


#--------------------------------------------------------------------------
'''

a = [1,1,4,5,1,4]


print(a[1])             #1


print(a[-1])            #4


print(a[0:3])           #[1,1,4]


print(a[5:])            #[4]


print(a[-3:])           #[5,1,4]


print("")

'''
#--------------------------------------------------------------------------

'''
print(a.index(4))       #2


print(a.count(1))       #3


print("")

'''
#--------------------------------------------------------------------------
'''

a.sort()                #sort from small to large


print(a)


a.sort(reverse=True)    #sort from large to small

'''

