# coding=utf-8
from selenium import webdriver
import time
from Tkconstants import CURRENT

sleepTime=2

# 打开firefox浏览器
driver = webdriver.Firefox()
# 打开百度页面
driver.get("https://www.baidu.com/")
# 等待页面加载完毕
time.sleep(sleepTime)
# 刷新页面
driver.refresh()
# 打开hao123页面
driver.get("https://www.hao123.com/")
time.sleep(sleepTime)
driver.refresh()
# 返回上一页
driver.back()
time.sleep(sleepTime)
# 返回下一页
driver.forward()
time.sleep(5)
# 设置屏幕尺寸
driver.set_window_size(560, 960, CURRENT)
time.sleep(sleepTime)
# 最大化窗口
driver.maximize_window()
time.sleep(sleepTime)
driver.refresh()
# 截图并指定路径、文件名保存
driver.get_screenshot_as_file("E:\\clt_test\\1.png")
# 退出浏览器，close()是关闭当前访问页面，quit()是退出浏览器，结束进程，且回收临时文件
driver.quit()
