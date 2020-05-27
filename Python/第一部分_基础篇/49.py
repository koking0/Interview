#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/27 11:40
# @File     : 49.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Stack:
	def __init__(self):
		self.stack = []

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		if self.stack:
			self.stack.pop()
		else:
			raise LookupError("Stack is Empty!")

	def top(self):
		return self.stack[-1]

	def isEmpty(self):
		return bool(self.stack)
