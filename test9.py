# -*- code =utf-8 -*-
# @Time :2023/5/1122:17
# @Auther :世界上最帅的男人
# @File :test9.py
# @Software :PyCharm

# 元组
"""
info = {"name": "吴彦祖", "age": 18}
print(info["name"])
print(info.get('age'))
print(info.get('gander', 'abc'));
print(info.get('age', 30))
"""

# 增
'''
info = {"name": "吴彦祖", "age": 18}
newID = input('请输入')
info['ID'] = newID
print(info.get('ID'))
'''

#删
'''
info = {"name": "吴彦祖", "age": 18}

del info["name"]                           #删除整个属性
print(info.get('name'))
info.clear()
print(info)                              #清空
'''

#改
'''
info = {"name": "吴彦祖", "age": 18}
info["name"]='xuwei'
print(info.get('name'))
'''

#查
info = {"name": "吴彦祖", "age": 18,'ID':325}
print(info.keys())
print(info.values())
print(info.items())
for key in info.keys():
    print(key)
print(info.__len__())