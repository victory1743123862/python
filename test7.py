# -*- code =utf-8 -*-
# @Time :2023/4/1119:12
# @Auther :世界上最帅的男人
# @File :test7.py
# @Software :PyCharm
# 打开网页
import sys
import webbrowser

sys.path.append("libs")
url = 'https://www.baidu.com'
for a in url:
    webbrowser.open(url)
print(a.get())
