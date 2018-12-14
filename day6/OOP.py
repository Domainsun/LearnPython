import time
class C():
    name=1
    def __init__(self,name):
        self.name=name

c1=C(1);
C.name=2
del c1.name
print(c1.name)

C.name=123
print(c1.name)

c2=C(111);
print(c2.name)

## __del__析构函数：在示例结尾释放，销毁的时候执行，通常用于做一些结尾工作

class C():
    name="domain"
    def __init__(self):
        pass
    def __del__(self):
        print("示例释放")

c1=C()

del c1

# time.sleep(10)

print(c2.name)

### 广度优先  横向 执行所有  继承的类
### 深度优先  纵向 执行所有  继承的类

## 多继承 ，广度优先(3.x)，深度优先(2.x)
#  python 2.x 的经典类时深度优先继承， 新式类按广度优先继承
#  python 3.x 的经典类 新式类按广度优先继承


# 类都特殊方法

## staticmethod 静态方法 在类里面的静态方法，用staticmethod 修饰

class Demo():
    @staticmethod
    def fun(name):
        print(name)
Demo.fun("domain")

## classmethod 类方法 在类里面的类方法，用classmethod修饰，只能访问 类变量，不能访问示例变量

class Demo():
    name="domain"
    def __init__(self,name):
        self.name=name

    @classmethod
    def fun(self):
        print(self.name)
d=Demo("alex")
d.fun()

## property 类属性方法 property，把一个方法变成一个静态属性调用，用于类属性的get和set


class Demo():

    def __init__(self):
        # self.name=name
        pass

    @property
    def get_name(self,name):         #property get值
        return self.name

    @get_name.setter                 #.setter set值
    def set_name(self, name):
        self.name = name

    @get_name.deleter                #deleter del值
    def del_name(self, name):
        del self.name

d=Demo()

d.name="domain"
print(d.name)
print(d.name)
del d.name

# 类的特殊方法
# __doc__    输出类描述信息
# __module__    输出当前使用的类是哪个模块里面的
# __class__    输出类本身
# __call__    通过对象的 对象() 调用__call__方法
class Demo():
    def __call__(self, *args, **kwargs):
        print(args,kwargs)
d=Demo()
d(1,2,3,4,name='domain',age=1)

# __dict__

class Demo():
    def __init__(self):
        pass
print(Demo.__dict__) #输出类所有属性
d=Demo()
print(d.__dict__)  #输出实例所有属性

# __str__   自定义类对象的输出信息
class Demo():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "<obj:%s>"%self.name
d=Demo("domain")
print(d)

# ____   可以通过字典的形式给对象赋值
class Demo():
    def __init__(self):
        self.data={}
    def __setitem__(self, key, value):  #添加字典元素
        self.data[key]=value
    def __getitem__(self, key):         #获取字典元素
        print(self.data[key])
    def __delitem__(self, key):         #删除字典元素
        del self.data[key]
d=Demo()
d['name']='domain'
d['age']=18
print(d['name'])
del d['age']

# 类的起源 python中一切皆对象,类也是一个对象，来自于类type，是类type的对象

print(type(Demo))  # 表示类Dome 来自于type<class 'type'>

# 通过type创建一个类
def talk(self):       #定义类talk方法
    print(self.name)
def __init__(self,name,age):    #定义类__init__ 构造方法
    self.name=name
    self.age=age
Demo = type('Demo',(object,),{'talk':talk,'__init__':__init__})   #通过type创建一个类，传入：类名，继承的类，类的方法
d=Demo('domain',17)
d.talk()

# 元类 ，用于自己定制类的创建  ps:没学会

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 反射
#hasattr()
#getattr()
#setattr()
#delattr()


class Demo():
    name='alex'
    def __init__(self):
        pass
d=Demo()
chioce=input("please input a String:")
if hasattr(d,chioce):
    print(getattr(d,chioce))
    setattr(d,chioce,'domain')
    print(getattr(d, chioce))
else:
    setattr(d,chioce,'domain')
chioce=input("please input a String:")
if hasattr(d,chioce):
   delattr(d,chioce)
   print(getattr(d,chioce))









