import  time
user,password='domain','123'
def auth(type):
    print("type",type)
    def out(func):
        def decor(*args,**kwargs):
            if type=="1":
                username=input('please input your name')
                userpassword=input('please input your password')
                if user==username and password==userpassword:
                    print('passed auth')
                    res=func()
                    return res
                else:
                    print('you username or password invaild.')
            elif type=="2":
                print("type ==2 ")
                username = input('please input your name')
                userpassword = input('please input your password')
                if user == username and password == userpassword:
                    print('passed auth')
                    res = func()
                    return res
                else:
                    print('you username or password invaild.')
        return decor
    return out

@auth("2")
def bbs():
    print("welcome to bbs")

bbs()

def auth(type):
    def timer(func):
        def decorator(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('spend time : %s' % (end_time - start_time))
        return decorator
    return timer

def func1():
    time.sleep(1)
    print('in the func1')



# func1()=auth("1")


func1 = auth("1")(func1)
func1()