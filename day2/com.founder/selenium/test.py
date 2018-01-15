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


import time
from selenium import webdriver


# 打开浏览器
chrome = webdriver.Chrome()

chrome.get("http://www.baidu.com/")

time.sleep(5)

chrome.close()