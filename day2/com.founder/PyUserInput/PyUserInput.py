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
import time

__author__ = 'gongmb'

from pymouse import PyMouse

m = PyMouse()
m.position()  # 获取当前的鼠标坐标
time.sleep(1)
m.move(1153, 538)
time.sleep(1)
m.click(1153, 538)  # 模拟点击
time.sleep(1)
m.press(1153, 538)  # 按下鼠标
time.sleep(1)
m.release(1153, 538)  # 释放鼠标
time.sleep(1)
