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

from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选之
inputs = dr.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
        time.sleep(1)
time.sleep(2)

dr.quit()