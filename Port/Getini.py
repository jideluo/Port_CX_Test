import configparser


#保存ini文件数值参数
class Person:
    def __init__(self):
        self.url =''

def getini (config_file_path,servicer):
    conf =configparser.ConfigParser()
    conf.read(config_file_path)#读文件
    url = conf.get(servicer,'url')#获取文件URL值
    Person.url=url;
    return url
