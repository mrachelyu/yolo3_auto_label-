# !/usr/bin/env python
# -*- coding: UTF-8 -*-

# 首字母要大寫
class Calculator:

    # 這兩行是class自己的東西
    # 因為有__init__，值被預先改掉

    name = 'Good Calculator'
    price = 1000

    def __init__(self, name, price, height, width, weight):
        self.name = name
        self.price = price
        self.h = height
        self.w =width
        self.weight = weight

    
    def add(self, x, y):
        print(self.name)
        result = x + y
        print("result:", result)

    def minus(self, x, y):
        result = x - y
        print("result:", result)

    def times(self, x, y):
        print("result:", x*y)

    def divide(self, x, y):
        print("result:", x/y)





def main():
    # class中的self = cal
    # 後面的參數分別對應到__init__中的 name, price, height, width, weight
    cal = Calculator('bad calculator', 18, 17, 16, 15)

    print(cal.name)
    print(cal.price)

    cal.add(10,20)
    cal.minus(10,20)
    cal.times(10,20)
    cal.divide(10,20)





if __name__ == "__main__":
    main()

