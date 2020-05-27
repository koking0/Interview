#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/22 19:14
# @File     : 31.lambda表达式与深浅拷贝的应用.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def num():
	return [lambda x: i * x for i in range(4)]


print([m(2) for m in num()])
