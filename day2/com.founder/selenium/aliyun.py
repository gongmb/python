# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main.py
   Description :    阿里云敏感词监测
   Author :       gongmb
   date：          2017/4/1
-------------------------------------------------
   Change Activity:
                   2017/4/1:
-------------------------------------------------
"""
from selenium.webdriver.common.by import By

__author__ = 'gongmb'

# https://promotion.aliyun.com/ntms/act/lvwangdemo.html?spm=5176.55804.911092.btn3.2b2557b4c9z0KZ

import time
from selenium import webdriver
from pymouse import PyMouse

# 模拟登陆163邮箱
from selenium.webdriver.common.keys import Keys

sleepTimeNumber = 2

driver = webdriver.Chrome()
driver.get("https://promotion.aliyun.com/ntms/act/lvwangdemo.html?spm=5176.55804.911092.btn3.2b2557b4c9z0KZ")
time.sleep(sleepTimeNumber)
driver.maximize_window()
m = PyMouse()
m.position()  # 获取当前的鼠标坐标
m.move(1049, 418)
m.click(1049, 418)  # 模拟点击

# elem_user = driver.find_element_by_name("email")
textarea = driver.find_element_by_class_name("text-check-textarea")
textarea.send_keys("gongmbo")
m.move(450, 848)
time.sleep(sleepTimeNumber)
m.click(450, 848)  # 模拟点击
time.sleep(sleepTimeNumber)

#返回值 父节点
result = driver.find_element_by_class_name("json-viewer-container")
#返回值子节点集
results = driver.find_elements_by_tag_name('pre')
for resu in results:
    print resu.text
time.sleep(sleepTimeNumber)

driver.close()
driver.quit()
