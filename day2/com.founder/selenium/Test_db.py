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

# 用cx_Freeze即可，它和py2exe，py2app类似，不过是跨平台的，并且支持python3。 例子：
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="guifoo",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": build_exe_options},
      executables=[Executable("aliyun.py", base=base)])