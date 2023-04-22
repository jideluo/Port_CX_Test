# 时间转为秒显示类
# 创建者:Leon
# 创建日期：2017-08-22 11:04:13
# -*- coding: utf-8 -*-
# !/usr/bin/python



import time

def Timestamp():
 millis =str(round(time.time()*1000))
 return millis

