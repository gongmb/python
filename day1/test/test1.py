# coding=utf-8

import urllib
import requests;

import webbrowser as  web  # web是别名

content = urllib.urlopen("http://www.jd.com").read()

open('data.html', 'w').write(content)

# 打开刚才写入的文件data.html

web.open_new_tab("data.html");


print("zhangsan啊啊")