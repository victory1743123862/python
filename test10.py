# -*- code =utf-8 -*-
# @Time :2023/5/1414:12
# @Auther :世界上最帅的男人
# @File :test10.py
# @Software :PyCharm


# h函数

# 定义
'''
def printinto():
    print(".................................")
    print("python真不错")
    print(".................................")

printinto()


# 函数返回值
def divid(a, b):
    shang = a / b
    yushu = a % b
    return shang, yushu


shu, yu = divid(8, 5)
print("商：%d,余数：%d" % (shu, yu))
'''
#import test9


# 答应一条横线的语句
def t1():
    print("----------------------------")


# 写函数，通过输入的参数打印出自定义行数的横线
'''
def t2():
    num = int(input("请输入"))
    # if num
    for i in range(num):
        t1()
    i = i + 1


t2()
'''


# 写一个函数求三个数的和

def t3(a, b, c):
    sum = a + b + c
    # print(sum)
    return sum


t3(1, 2, 3)


# 写函数求三个数的平均值
def t4(a, b, c):
    a = t3(1, 2, 3)
    b = a / 3.0
    print("平均值为%d" % b)


t4(1, 2, 3)


