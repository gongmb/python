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

# 打开一个文件
fo = open("D:\\Test8\\SensitiveWord\\foo.txt", "a")
fo.write("www.runoob.com!\nVery good site!\n");

# 关闭打开的文件
fo.close()
