import pickle,json,os
def info():
    print("欢迎来到ATM系统")
    print("1.开户")
    print("2.存钱")
    print("3.取钱")
    print("4.退出")
    option=input("请输入对应数字进行操作")
    option_dic={
        '1':creat_account
    }
    if option in option_dic :
        option_dic[option]()
    else:
        print('请重新选择操作')

def creat_account():
    user =input('请输入用户名:')
    password =input('请输入密码:')
    info={
        "user":user,
        "password":password,
    }
    f = open(r"../conf/userinfo/" + user+".txt", "w")
    f.write(json.dumps(info))
    print('恭喜您%s 开户成功!'%user)
    f.close()

def other_option(tatal_money,expend_money,option):

    tatal_money


    return tatal_money

def exists_account(user):
    return os.path.exists(r"../conf/userinfo/" + user+".txt")

while True:
    info()
    print(exists_account("3"))










