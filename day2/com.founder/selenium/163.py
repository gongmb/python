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
from selenium import webdriver


# 模拟登陆163邮箱
from selenium.webdriver.common.keys import Keys

sleepTimeNumber=2

driver = webdriver.Chrome()
driver.get("http://mail.163.com/")
time.sleep(sleepTimeNumber)
driver.switch_to_frame('x-URS-iframe')  #需先跳转到iframe框架
# 用户名 密码
# time.sleep(sleepTimeNumber)
elem_user = driver.find_element_by_name("email")
elem_user.send_keys("gongmbo")
elem_pwd = driver.find_element_by_name("password")
elem_pwd.send_keys("gong7682696")
elem_pwd.send_keys(Keys.RETURN)
#然后向这个控件发送回车键，注意，如果是键盘上的回车，SHIFT，CONTROL键之类的，要用Keys.控制键的名称作为输入。
time.sleep(sleepTimeNumber)
# assert "baidu" in driver.title
driver.close()
driver.quit()