names=[]         #定义列表
dic={}           #定义字典
try:
    names[2]
    dic['name']
    n
except IndexError as e:  #列表索引异常
    print(e)
except KeyError as e:    #字典key异常
    print(e)
except Exception as e:   #所有异常
    print(e)
else:                   #没有异常时执行
    print('没有异常')
finally:                #有没有异常时都执行
    print('无论是否有异常都执行')

#自定义 异常
class CustomException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return 'Exception:%s'%self.msg
try:
    raise CustomException('Custom Exception!!!')
except CustomException as e:
    print(e)