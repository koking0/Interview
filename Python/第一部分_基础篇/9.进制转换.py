#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/21 17:25
# @File     : 9.进制转换.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# 二进制转换成十进制：v = '0b1111011'
v = '0b1111011'
print(int(v, 2))
# 十进制转换成二进制：v = 18
v = 18
print(bin(v))
# 八进制转换成十进制：v = '011'
v = '011'
print(int(v, 8))
# 十进制转换成八进制：v = 30
v = 30
print(oct(v))
# 十六进制转换成十进制：v = '0x12'
v = '0x12'
print(int(v, 16))
# 十进制转换成十六进制：v = 87
v = 87
print(hex(v))
