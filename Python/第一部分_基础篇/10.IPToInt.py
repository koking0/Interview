#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/21 17:33
# @File     : 10.IPToInt.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
print(int(''.join([bin(num).strip('0b').zfill(8) for num in list(map(int, input("Please Input IP:").split('.')))]), 2))
