# -*- code =utf-8 -*-
# @Time :2023/5/1415:54
# @Auther :世界上最帅的男人
# @File :test11.py
# @Software :PyCharm

import os

f =open("test.txt","r")
#for a in range(10):
    #a = f.write('hello world\n')
print(f.read(10))
print(f.readline())
print(f.readlines())

f.close()

f = open("test.txt")
os.rename("test.txt","TEST.txt")



