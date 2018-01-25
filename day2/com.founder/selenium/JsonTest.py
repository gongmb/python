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

import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = json.dumps(data)
print json

# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
#
# text = json.loads(jsonData)
# print text['a']
