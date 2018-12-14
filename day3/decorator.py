import time


# 装饰器 推导过程


def timer(func):
    def decorator(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print('spend time : %s' %(end_time-start_time))
    return decorator

@timer
def func1(name,age):
    time.sleep(1)
    print('in the func1,name is {_name} and age is {_age}'.format(_name=name,_age=age))


@timer
def func2():
    time.sleep(1)
    print('in the func2')



# func1=timer(func1)
func1("domain",18)
func2()











