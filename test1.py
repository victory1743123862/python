# -*- code =utf-8 -*-
# @Time :2023/4/616:56
# @Auther :世界上最帅的男人
# @File :test1.py
# @Software :PyCharm

password = input("请输入")
trueword = "123456"
if trueword == password:
    print("登录成功")
elif trueword != password:
    print("输入错误")

print(".................................................")
xinbie = 0 #1男生0女生
danshen = 1 #1单身0有对象
if xinbie == 1 :
	print("您是男生")
	if danshen ==1 :
		print("没对象哈哈哈哈哈哈哈哈")
	else :
		print("哪找的对象，过分")
else :
	print("您是女生")
	if danshen ==1 :
		print("给你介绍一个吧")
	else :
		print("真幸福")

