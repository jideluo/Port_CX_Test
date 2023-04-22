import urllib.request
import urllib.parse
import requests
import json
import  urllib3
import datetime


def post(url,data): #Post 请求
 data=urllib.parse.urlencode(data).encode('utf-8')
 re=urllib.request.Request(url,data)
 #urllib.request.Request.add_header('User-Agent', 'fake-client')
 html=urllib.request.urlopen(re)
 print(html.getcode(),html.msg)
 print(html.read())
 return html.msg

def postBody(url,body_value): #Post  bady_value 请求
    http = urllib3.PoolManager()
    # print(type(body_value)#判断数据类型
    print(url)
    print(body_value)
    encoded_data = json.dumps(body_value).encode('utf-8')
    start_time = datetime.datetime.now()  # 记录运行时间
    try:
        r = http.request(
            'POST',
            url=url,
            body=encoded_data,
            headers={'Content-Type': 'application/json'})

        if (r.status == 200):
            # print(json.loads(r.data.decode('utf-8')))
            jsondata = json.loads(r.data.decode('utf-8'))
            end_time = datetime.datetime.now()  # 记录结束时间
            operation_time = (end_time - start_time).microseconds / 1000000  # 将微妙转为秒
            # print(operation_time)  # 统计程序运行时间
            # print(type(jsondata))
            # print(jsondata['errorMessage'])
            print(jsondata)#y用于数据处理
            if ("errorMessage" in jsondata.keys()):
                return r.status, jsondata['errorMessage'], operation_time
            else:
                return r.status, jsondata['error'], operation_time  # 返回码存在error内容显示
        else:
            print(r.status)
            end_time = datetime.datetime.now()  # 记录结束时间
            operation_time = (end_time - start_time).microseconds / 1000000  # 将微妙转为秒
            print(operation_time)  # 统计程序运行时间
            return r.status, "Null", operation_time
    except Exception as err:
        print("断网了"+err)



