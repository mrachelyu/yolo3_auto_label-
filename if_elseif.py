 #!/usr/bin/env python
 #-*- coding: UTF-8 -*-
'''
string_A = 'abcd' + 'efgh' + 'ijkl' + 'mnop' + 'qrst' + 'uvwx' + 'yz'
string_B = 'abcd' + 'efgh'\
                + 'ijkl' + 'mnop'\
                + 'qrst' + 'uvwx' + 'yz'
# \換行

print("string_A: ", string_A)
print("string_B: ", string_B)
print("string_A = string_B ? ", string_A == string_B)
# 要print的東西，可以用條件寫，會回傳True/False
'''
# ======================
'''
x = 1
y = 2
z = 3
if x == y:
    print('x is equal to y')
'''
# ======================
'''
flag_A = True

if flag_A:
    print("This is in if")
else:
    print("This is in else")
'''
# ======================
'''
worked = True
status = 'Done.' if worked else 'Not yet.'
print("Status:", status)
# python沒有 condition ? value1 : value2 的用法
'''
# ======================
'''
number = 1
if number == 1:
    print("number = 1")
elif number == 10:
    print("number = 10")
else:
    print("number = ?")
'''
# ======================
'''
list_a = [1, 2, 4, 8, 10]
number = 10
if 3 < number < 12:
    if number != 7:
        if number <= 11:
            if number > 9 and number not in list_a:
            # and=且，in=在...裡，not in=不在...裡
                print("Hi there!")
'''

#=======================

score = eval(input("please enter the math fraction(0~100):"))

if score >= 90:
	print("excellent")
else:
	if score >= 80:
		print("best")
	else:
		if score >= 70:
			print("good")
				
