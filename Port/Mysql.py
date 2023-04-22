#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import datetime
import time
import configparser

def connectMysql():
    dbUlr= "TestMysql"
    conf = configparser.ConfigParser()
    conf.read("data.ini")  # 读文件
    gethost = conf.get(dbUlr,'host')  # 获取文件host值
    getport = int(conf.get(dbUlr,'port'))  # 获取文件port值
    getuser = conf.get(dbUlr,'user')  # 获取文件user值
    getpasswd = conf.get(dbUlr,'passwd')  # 获取文件passwd值
    getdb = conf.get(dbUlr,'db')  # 获取文件db值
    getcharset = conf.get(dbUlr, 'charset')  # 获取文件charset值
    try:
        connect=pymysql.connect(
        host=gethost,
        port=getport,
        user=getuser,
        passwd=getpasswd,
        db=getdb,
        charset=getcharset
        )
        print(gethost,getport,getuser,getdb,getcharset)
        print("成功连接数据库")
        return  connect

    except Exception as err:
        print(err)
def insertDb(datalist):
    connect=connectMysql()
    cursor = connect.cursor()
    timeNum=time.strftime('%H')
    try:
        for kv in datalist.items():
            data = (kv[0], float(kv[1][0]), kv[1][1], datetime.datetime.now(),timeNum)
            # 插入数据
            sql = "INSERT INTO postdb (FunctionName, AverageData, Netstat,CreatedTime,TimeNum) VALUES ( '%s', %.3f, %d ,'%s','%s')"
            cursor.execute(sql % data)
        print('成功插入数据')
    except Exception as err:
        print(err)
    connect.close()



