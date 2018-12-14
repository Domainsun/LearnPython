# 终结版

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


def index():
    print("welcome to index")

@auth("1")
def home():
    print("welcome to home")
    return "result form home "

@auth("2")
def bbs():
    print("welcome to bbs")

index()
print(home())
bbs()
