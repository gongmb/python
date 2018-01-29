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
import json
# 模拟登陆163邮箱

from selenium.webdriver.common.keys import Keys

# 全局变量
sleepTimeNumber = 2

print "程序开始执行"
print "待检测的敏感词库"
# 待检测的敏感词库
list = []  ## 空列表
txt = open("F:\\Test8\\SensitiveWord\\SensitiveWord_2.txt", "r")
line = txt.readline()
while line:
    list.append(line)
    line = txt.readline()
print len(list)
print "敏感词库输入完成"
driver = webdriver.Chrome()
driver.get("https://promotion.aliyun.com/ntms/act/lvwangdemo.html?spm=5176.55804.911092.btn3.2b2557b4c9z0KZ")
time.sleep(sleepTimeNumber)
driver.maximize_window()
m = PyMouse()
m.position()  # 获取当前的鼠标坐标
m.move(1049, 418)
m.click(1049, 418)  # 模拟点击

textarea = driver.find_element_by_class_name("text-check-textarea")

bs = 0

for x in list:
    textarea.clear()
    textarea.send_keys(x.decode('utf-8').replace("\n", ""))
    m.move(450, 848)
    time.sleep(sleepTimeNumber / 2)
    m.click(450, 848)  # 模拟点击
    time.sleep(sleepTimeNumber / 2)

    resultJson = ""
    # 返回值 父节点
    result = driver.find_element_by_class_name("json-viewer-container")
    # 返回值子节点集
    results = driver.find_elements_by_tag_name('pre')
    for resu in results:
        resultJson = resu.text

    replace = resultJson.replace("\n", "")
    replace = replace.replace(" ", "")

    # 阿里云监测结果保存到文件中
    # 检测完成以后的词库保存在这里
    # 打开一个文件
    detection = open("F:\\Test8\\SensitiveWord\\detection.txt", "a")
    detection.write(x.replace("\n", ""))
    detection.write('--')
    detection.write(replace.encode("utf-8"))
    detection.write('\n')
    # 关闭打开的文件
    detection.close()

    print(replace)
    text = json.loads(replace)

    label_ = text['data'][0]['results'][0]['label']
    suggestion_ = text['data'][0]['results'][0]['suggestion']
    print label_
    print suggestion_
    bs = bs + 1
    if bs == 100:
        bs = 0
        driver.refresh()
        m = PyMouse()
        m.move(1049, 135)
        m.click(1049, 135)  # 模拟点击
        textarea = driver.find_element_by_class_name("text-check-textarea")

time.sleep(sleepTimeNumber)

driver.close()
driver.quit()
