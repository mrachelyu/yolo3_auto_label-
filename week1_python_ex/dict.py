# !/usr/bin/env python
# -*- coding: UTF-8 -*-

# dict包含沒有順序、沒有重複，且可改變內容的多個鍵：值對，屬於對映型別
# dict的key, value，型態不需一致

dict_a = {}             
dict_b = dict()        


dict_c = {"Key_1": 1, "Key_2": 2.0, "Key_3": "3"}
print("type(dict_c):", type(dict_c))
print("len(dict_c):", len(dict_c))      
print("dict_c:", dict_c)


print("dict_c.items():", list(dict_c.items()))
print("dict_c.keys():", list(dict_c.keys()))
print("dict_c.values():", list(dict_c.values()))

# catch dict的value，並delete 該term
val = dict_c.pop("Key_1")
print("dict_c.pop(""Key_1""):", val)
print("dict_c:", dict_c)


'''
# ======================
'''
# list和tuple須是string
# list和tuple裡，每組只能有兩個字元，才能變成dict
dict_c = {"Key_1": 1, "Key_2": 2.0, "Key_3": "3"}
list_a = ['12', '34', '56']
tuple_a = ('ab', 'cd', 'ef')
dict_d = dict_c         # or dict_d = dict(dict_c)
dict_e = dict(list_a)
dict_f = dict(tuple_a)
print("dict_d:", dict_d)
print("dict_e:", dict_e)
print("dict_f:", dict_f)
print("dict_e.items():", list(dict_e.items()))
print("dict_e.keys():", list(dict_e.keys()))
print("dict_e.values():", list(dict_e.values()))
print("dict_f.items():", list(dict_f.items()))
print("dict_f.keys():", list(dict_f.keys()))
print("dict_f.values():", list(dict_f.values()))
'''
# ======================
'''
dict_c = {"Key_1": 1, "Key_2": 2.0, "Key_3": "3"}
print(dict_c["Key_2"])

# 新增term
dict_c["Key_4"] = 'four'
print(dict_c["Key_4"])

# 修改某個term的value
dict_c["Key_4"] = 'FOUR'
print(dict_c)
'''
# ======================
'''
list_a = ['12', '34', '56']
tuple_a = ('ab', 'cd', 'ef', '17')
dict_e = dict(list_a)
dict_f = dict(tuple_a)
print("dict_e:", dict_e)
print("dict_f:", dict_f)
# update dict_e
# 如果被更新和想更新的dict中有一樣的key，則被更新的dict該key的value會被覆蓋
dict_e.update(dict_f)
print("dict_e:", dict_e)
'''
# ======================
'''
list_a = ['12', '34', '56']
dict_e = dict(list_a)
print("dict_e:", dict_e)

# delete a item in dict
# 只能用key刪
del dict_e['1']
print("dict_e:", dict_e)

# 清空字典所有term
dict_e.clear()
print("dict_e:", dict_e)

# 删除字典
del dict_e

