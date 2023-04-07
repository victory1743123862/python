# -*- code =utf-8 -*-
# @Time :2023/4/720:51
# @Auther :世界上最帅的男人
# @File :test4.py
# @Software :PyCharm

# 九九乘法表
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(a)):
    for i in range(len(b)):
        if b > a:
            c = a * b
         #   print(c, end='\t')
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='  ')
    print(' ')
