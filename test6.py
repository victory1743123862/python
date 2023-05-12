# -*- code =utf-8 -*-
# @Time :2023/4/1019:16
# @Auther :世界上最帅的男人
# @File :test6.py
# @Software :PyCharm

# 列表
'''
alist = [1, 23, '儿歌', 45, 'dwe']
print(alist[2])
print(alist[3])
for a in alist:
    print(a)
print(len(alist))

# 增
alist.append(88)
alist.insert(2, 'dahuang')
b = [2, 3, 4, 5, 6, ]
alist.extend(b)
# 删
del alist[0]
# 改
alist[4] = 77
for a in alist:
    print(a, end='\t')
# 查
name = input('请输入要查的数据')
if name in alist:
    print('存在')
else:
    print('错误')
print('儿歌' in alist)
print(alist.index(23, 0, 4))
'''

alist = [12, 3, 4, 3, 7, 1, 7, 9]
#alist.sort(reverse=False)
print(alist)
alist.reverse()
print(alist)