# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main.py
   Description :
   Author :       gongmb
   date：          2017/4/1
-------------------------------------------------
   Change Activity:
                   2017/4/1:
-------------------------------------------------
"""
__author__ = 'gongmb'
import sys

# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
#
# print "list1[0]: ", list1[0]
# print "list2[1:5]: ", list2[1:5]

# list = []          ## 空列表
# list.append('Google')   ## 使用 append() 添加元素
# list.append('Runoob')
#
# list1 = ['physics', 'chemistry', 1997, 2000]
#
# print list1
# del list1[2]
# print "After deleting value at index 2 : "
# print list1

# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代

list = []          ## 空列表


# txt = open("D:\\Test8\\SensitiveWord\\SensitiveWord_2.txt", "r")
# line = txt.readline()
# while line:
#     list.append(line)  ## 使用 append() 添加元素
#     line = txt.readline()
#
# print len(list)


txt = open("D:\\Test8\\SensitiveWord\\SensitiveWord_2.txt", "r")
line = txt.readline()
while line:
    list.append(line)  ## 使用 append() 添加元素
    line = txt.readline()

print len(list)