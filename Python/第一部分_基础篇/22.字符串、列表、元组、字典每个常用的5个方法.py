#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/22 8:18
# @File     : 22.字符串、列表、元组、字典每个常用的5个方法.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
words = "today is a wonderfulday"
print(words.strip('today'))  # 如果strip方法指定一个值的话，那么会去掉这两个值
print(words.count('a'))  # 统计字符串出现的次数
print(words.index('is'))  # 找下标
print(words.index('z'))  # 找下标如果元素不找不到的话，会报错
print(words.find('z'))  # 找下标，如果元素找不到的话，返回-1
print(words.replace('day', 'DAY'))  # 字符串替换

