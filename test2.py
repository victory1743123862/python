# -*- code =utf-8 -*-
# @Time :2023/4/622:40
# @Auther :世界上最帅的男人
# @File :test2.py
# @Software :PyCharm
# 石头剪刀布小游戏 剪刀（0） 石头（1） 布（2）
print(".............................................")
print("请选择：剪刀（0） 石头（1） 布（2）")
a = input("请输入您的选择")
import random
b = random.randint(0, 2)
print(b)
if a == "1" :
    if b == "0" :
        print("恭喜您赢了")
    elif  b == "1":
        print("平局")
    else:
        print("您输了")
elif a == "2" :
    if  b == "1":
        print("哈哈哈您输了")
    elif  b == "2":
        print("平局")
    else:
        print("您输了")
elif a == "0" :
    if a == "0":
        print("平局")
    elif  b == "2":
        print("您赢了")
    else:
        print("您输了")
else:
        print("对不起请重新输入")
print(".............................................")
