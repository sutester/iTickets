#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danny
@contact: kedanlin@hotmail.com
@file: split_text.py.py
@time: 2019/5/23 21:42
@desc:
'''
img_key = '对应'
math_key = '计算'
str1 = '请点击计算的结果XXX'
str2 = '请点击对应的两个图片XXX'
if img_key in str1:
    question = str1.split('计算的')[1]
else:
    question = str2.split('对应的')[1]

print(question)