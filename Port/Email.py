# 邮件发送功能类
# 创建者:Leon
# 创建日期：2017-08-22 11:04:13
# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

my_sender = 'li_****@126.com'  # 发件人邮箱账号
my_pass = '*******'  # 发件人邮箱密码
my_user = '151********@139.com'  # 收件人邮箱账号，我这边发送给自己
CCADDR = ['151********@@139.com', 'li_****@126.com']
def SendMail():
    f = open('TestResult.txt')
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = formataddr(["POSTTest调试", my_sender])
    message['To'] = formataddr(["leon", "151********@@139.com"])
    subject = '【智能短信每日接口检测测试报告_' + time.strftime("%Y%m%d") + '】'  # 邮件标题
    message['Subject'] = Header(subject, 'utf-8')
    if(f.read()!="0"):#接口异常时发送邮件，抄送给接口人
        message['Cc'] = ', '.join(CCADDR)
        message.attach(MIMEText('附件为每日接口测试报告，接口测试异常，请查看接口测试报告！', 'plain', 'utf-8'))
    elif(time.strftime('%H')=="10"):#每天10点发送接口测试报告，并抄送给接口人
        message['Cc'] = ', '.join(CCADDR)
        message.attach(MIMEText('附件为每日接口测试报告，接口测试正常，请各位知悉！', 'plain', 'utf-8'))
    else:
        message.attach(MIMEText('附件为每日接口测试报告，接口测试正常，请各位知悉！', 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('PostTest.xlsx', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename='+"PostTest_"+time.strftime("%Y%m%d")+".xlsx"
    message.attach(att1)
    try:
        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
def testTime():
    print(time.strftime('%H')=="16")

if __name__ =='__main__':
    testTime()