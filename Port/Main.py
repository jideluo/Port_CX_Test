# from MD5 import get_md5_value
# from Timestamp import  Timestamp
from Post import  post,postBody
from Getini import getini, Person
from GetExcel import OpenExcel
from Email import SendMail
import datetime
import time

def getExcleAction(servicer_url,Excel_File,Operation_Number):#Excel文本形式请求数据
    print("[Excel文本形式请求数据]")
    print(servicer_url)
    print(Excel_File)
    OpenExcel(servicer_url,Excel_File, Operation_Number)

def getInitActiontest(servicer_url):#模版初始化
    print("[模版初始化]")
    print(servicer_url)
    # print(Excel_File)
    # OpenExcel(servicer_url,Excel_File)
    url2 = 'template/init.action'
    url = servicer_url + url2
    body_value ={"requestId":"1","appId":"100002","clientVersion":"2.5.0","sign":"4aba5b7e177de448d16cdca01607a1de","clientId":"1","from":"1","version":"1","deviceId":"1","terminal":"1","condition":{"ports":["10086","95508","10010","95588","95555","95533"]}}
    postBody(url,body_value)


if __name__ =='__main__':
    start_time = datetime.datetime.now()#记录运行时间
    print(start_time)
    servicer_url= getini('data.ini','Dev')#传入文件路径和测试类型
    Excel_File="PostTest.xlsx"
    Operation_Number =5  #默认运行5次
    getExcleAction(servicer_url,Excel_File,Operation_Number) #模版初始化
    # getInitActiontest(servicer_url)  # 模版初始化
    end_time = datetime.datetime.now()#记录结束时间
    print((end_time-start_time).microseconds/1000000)#统计程序运行时间
    SendMail()#发送邮件

