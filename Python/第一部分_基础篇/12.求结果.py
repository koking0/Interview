#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/21 19:41
# @File     : 12.求结果.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
v1 = 1 or 3
print(f'v1 = {v1}')
v2 = 1 and 3
print(f'v2 = {v2}')
v3 = 0 and 2 and 1
print(f'v3 = {v3}')
v4 = 0 and 2 or 1
print(f'v4 = {v4}')
v5 = 0 and 2 or 1 or 4
print(f'v5 = {v5}')
v6 = 0 or False and 1
print(f'v6 = {v6}')
