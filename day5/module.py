import  time,datetime,random,os,sys
time_now=time.time()
### 当前时间戳
print()
print(time.localtime())


help(time)
dir(time)
# a=time.asctime(Sat Jun 06 16:26:11 1998)
# 当前时间戳
time.time()
# 当前 UTC 时间,传入时间戳返回元组UTC 时间
time.gmtime()
# 当前UTC+8（北京时间） 时间、传入时间戳返回元组北京时间
time.localtime()
# 元组格式时间 转换成时间戳

# time=time.localtime(time.time())
# print(time)
time_now=time.localtime()
print(time_now)
# 传入元组时间返回时间戳
print(time.mktime(time.localtime()))

# 元组时间变成格式化字符串 ,传入元组，返回格式化字符串 2018-04-23 21:55:15
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 格式化时间转换成元组时间 ,传入格式化时间，返回元组时间 time.struct_time(tm_year=2018, tm_mon=4, tm_mday=23, tm_hour=21, tm_min=56, tm_sec=40, tm_wday=0, tm_yday=113, tm_isdst=-1)
print(time.strptime("2018-04-22 21:56:40","%Y-%m-%d %H:%M:%S"));

# 传入元组 转换成 固定格式：Mon Apr 23 22:18:56 2018
print(time.asctime())
# 传入时间戳 转换成 固定格式：Mon Apr 23 22:18:56 2018
print(time.ctime())


# datetime 获取当前时间
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))
print(datetime.datetime.now()+datetime.timedelta(-3))

### 0-1（不包括1）随机数

print(random.random())

### 指定随机范围int 随机数 包括第二个参数
print(random.randint(1,10))

### 指定随机范围float 随机数 包括第二个参数
print(random.uniform(1,10))

# 指定随机范围随机数 不包括第二个参数
print(random.randrange(1,3))

# 取随机序列对象，字符串，列表，元组等
print(random.choice('domain'))
### 取指定个数随机序列对象，字符串，列表，元组等
print(random.sample('domain',2)) #['o', 'i']



###
# print(os.getcwd()) #F:\PyWorkSpace\day5
#
# os.chdir(r"c:\users")
# print(os.getcwd())
# print(os.curdir)
# print(os.pardir)
# print(os.pardir)
#
#
# os.makedirs(r"e:\Users\111\222")
# os.remove(r"e:\Users\111")  #为空则删除
#
# os.mkdir(r"e:\Users\aaa)
# os.mkdir(r"e:\Users\aaa\bbb)
#
# os.rmdir(r"e:\Users\aaa\bbb)
# os.listdir(".")
# os.listdir("c:")
#
# os.remove(r"C:\Users\sunlo\Desktop\mainActivity.txt")
# os.rename("oldName","newName")
# os.stat("path/fileName")
#
# ### 获取当前系统文件分隔符
# os.sep
# ### 获取当前系统换行符
# os.linesep
# ### 获取当前系统环境变量分隔符
# os.pathsep
# ### 获取当前系统名字
# os.name
# ### 调用当前系统命令
# os.system()
# ### 获取当前系统环境变量
# os.environ
#
# ### 获取当前文件绝对路径
# os.path.abspath(__file__)
#
# ### 分割成路径和文件 为一个元组
# os.path.split()
#
# ### 取字符串里面的路径
# os.path.dirname(r'c:\a\b)
# ### 取取字符串里面文件
# os.path.basename()
#
# ### 判断文件是否存在
# os.path.exists()
# ### 判断文件是否为绝对路径
# os.path.isabs()
# ### 判断是否为文件夹
# os.path.isdir()
# ### 判断是否为文件
# os.path.isfile()
# ### 拼接路径和文件
# os.path.join()
# ### 获取文件创建时间
# os.path.getatime()
# ### 获取文件修改时间
# os.path.getmtime()
#
# 获取脚本名字

# 获取参数列表
sys.argv
# 获取python解释程序的版本信息
sys.version
sys.maxsize




