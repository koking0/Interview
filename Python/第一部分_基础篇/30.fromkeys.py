#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/22 19:03
# @File     : 30.fromkeys.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
v = dict.fromkeys(['k1', 'k2'], [])
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)
