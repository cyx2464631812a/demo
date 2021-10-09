import random
import time
while True:
    num = float(input("请输入华氏度"))
    t = (num - 32) * 5 / 9
    print(t)

print("\n")
while True:
    num = float(input("请输入圆半径"))
    S = 3.14 * num ** 2
    C = 2 * 3.14 * num
    print("s",S)
    print("c",C)

print("\n")
while True:
    num = float(input("请输入年份"))
    if (num % 400) == 0:
        print("闰年")
    elif (num % 100) == 0:
        print("不是闰年")
    elif (num % 4) == 0:
        print("闰年")
    else:
        print("不是闰年")

print("\n")
while True:
    num = float(input("请输入英寸"))
    Y = num * 2.54
    print(Y,"cm")

print("\n")
while True:
    num = float(input("请输入成绩"))
    if num >= 90:
        print("A")
    elif num >= 80 and num < 90:
        print("B")
    elif num >= 70 and num < 80:
        print("C")
    elif num >= 60 and num < 70:
        print("D")
    else:
        print("E")

print("\n")
import math
while True:
    A = float(input("请输入边长a",))
    B = float(input("请输入边长b",))
    C = float(input("请输入边长c",))
    if A + B > C and B + C > A and A + C > B :
        zc = A+B+C
        S_sqrt = (((A + B + C) / 2 * ((A + B + C) / 2 - A) * ((A + B + C) / 2 - B) * ((A + B + C) / 2 - C)))** 0.5
        print("周长",zc)
        print("面积",S_sqrt)