# !/usr/bin/env python
# -*- coding: UTF-8 -*-

#def = define


def do_nothing():
   pass

def say_something():
   print("nice to neet you")

def agree():
   return True

def echo(input):
   return str(input) + " " + str(input)

def is_none(thing):
   if thing is None:
       #print("It's None.")
       return None
   elif thing :
       #print("It's True.")
       return True
   else:
       #print("It's False.")
       return False

def menu(wine, entree, dessert):
   return {"wine":wine, "entree":entree, "dessert":dessert}

def menu_today(wine, entree, dessert="pudding"):
   return {"wine":wine, "entree":entree, "dessert":dessert}

def buggy(arg, result=[]):
   result.append(arg)
   return result

def buggy_2(arg):
   result=[]
   result.append(arg)
   return result

def print_arg(*args):
   print("Positional argument tuple: ", args)

def print_more_arg(input_1, input_2, *args):
   print("Input 1 is: ", input_1)
   print("Input 2 is: ", input_2)
   print("All the rest: ", args)

def printkwargs(**kwargs):
   print("Keyword arguments:", kwargs)

def print_if_true(input, check):
   '''
   Print the first argument if a second argument is true.
   '''
   if check:
       print(input)

def sum_args(*args):
   return(sum(args))

def run_with_positional_args(func, *args):
   return func(*args)

def main():

   '''
   if agree():
       say_something()
   else:
       print(echo(2))
       print(do_nothing())
   '''
   '''
   type_list = [None, True, False, 0, 0.0, (), [], {}, set()]

   for thing in type_list:
       print(str(thing) + ' is ', str(is_none(thing)))
   '''
   '''
   print(menu("chardonnay", "chicken", "cake"))
   print(menu(dessert="cake", wine="chardonnay", entree="chicken"))
   print(menu_today("chardonnay", "beef"))
   print(menu_today("chardonnay", "beef", dessert="cake"))
   '''
   '''
   print(buggy('a'))
   print(buggy('b'))

   print(buggy_2('a'))
   print(buggy_2('b'))
   '''
   '''
   print_more_arg("hello", 1, 2, 3)
   '''
   '''
   dict_a = {"wine":"chardonnay", "entree":"chicken", "dessert":"cake"}
   print(dict_a)
   printkwargs(wine="chardonnay", entree="chicken", dessert="cake")
   printkwargs(**dict_a)  
   '''
   '''
   print(print_if_true.__doc__)
   '''
   '''
   print(run_with_positional_args(sum_args, 1, 2, 3, 4))
   '''







if __name__ == "__main__":   #當作為模塊被呼叫時，輸入這兩行main()可避免也被執行
   main()

#if 啟動＝true
#if 外部呼叫 = false
#有打有保障 


'''
========分隔線========
'''
#練習1：最大公因數

def gcd(m, n):
   if n == 0:
       return m
   else:
       return gcd(n, m % n)

print(gcd(20, 30))         #  10
print(type(gcd))           # 顯示 <class 'function'>

gcd2 = gcd
print(gcd2(20, 30))        #  10
print(id(gcd), id(gcd2))   # 兩個顯示的數字相同

'''
========分隔線========
'''
#練習2：由小排到大

def selection(number):
   # 找出排序中最小值
   def min(m, j):
       if j == len(number):
           return m
       elif number[j] < number[m]:
           return min(j, j + 1)
       else:
           return min(m, j + 1)
  
   for i in range(0, len(number)):
       m = min(i, i + 1)
       if i != m:
           number[i], number[m] = number[m], number[i]

number = [1, 5, 2, 3, 9, 7]
selection(number)
print(number)     #  [1, 2, 3, 5, 7, 9]



