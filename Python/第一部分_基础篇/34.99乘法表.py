#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/22 23:13
# @File     : 34.99乘法表.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
print('\n'.join(['\t'.join([f'{row} * {col} = {row * col}' for col in range(1, row + 1)]) for row in range(1, 10)]))
