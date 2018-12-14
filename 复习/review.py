# coding=gbk
def setDemo():
    """

    """

    set1 = set([1, 2, 1, 1, 13, 4, 111])
    print(set1)


def dicDemo():
    '''
    字典(dict)代码示例
    注意:
        1.可以重复key，当重复key 时, 覆盖之前的的key,value，以最后一次赋值为准
        2.无序
        3.key不可变，可是key可以用数字，字符串或元组充当，但是就是不能使用列表
        4.value可以为任意类型

    方法和函数	描述
        cmp(dict1, dict2)	比较两个字典元素
        len(dict)	计算字典元素个数
        str(dict)	输出字典可打印的字符串表示
        type(variable)	返回输入的变量类型，如果变量是字典就返回字典类型
        dict.clear()	删除字典内所有元素
        dict.copy()	返回一个字典的浅复制
        dict.values()	以列表返回字典中的所有值
        popitem()	随机返回并删除字典中的一对键和值
        dict.items()	以列表返回可遍历的(键, 值) 元组数组
    '''
    dict1 = {
        'name': "domain",
        'name': "alex",
        'age': 1
    }
    print(dict1)
    print('name is %s' % dict1['name'])


def ifDemo():

    num = 0
    if num:  # 非零数值、非空字符串、非空 list 等，判断为True，否则为False
        print('hello world')
    java = 86
    python = 68

    if java > 80 and python > 80:
        print('优秀')
    else:
        print('不优秀')

    if (java >= 80 and java < 90) or (python >= 80 and python < 90):
        print('良好')

def lambdaDemo():
    """
    lambda :匿名函数

    :return:
    """          #:前是传入的参数, :后是表达式,返回值为表达式的计算值
    sum = lambda num1, num2: num1 + num2+3;
    print(sum(1, 2))

def funcDemo():
    """
    在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象。
    不可更改的类型：
        变量赋值 a = 1，其实就是生成一个整形对象 1 ，然后变量 a 指向 1，当 a = 1000 其实就是再生成一个整形对象 1000，然后改变 a 的指向，不再指向整形对象 1 ，而是指向 1000，最后 1 会被丢弃
    可更改的类型：
        变量赋值 a = [1,2,3,4,5,6] ，就是生成一个对象 list ，list 里面有 6 个元素，而变量 a 指向 list ，a[2] = 5则是将 list a 的第三个元素值更改,这里跟上面是不同的，并不是将 a 重新指向，而是直接修改 list 中的元素值。
    :return:
    """
    def print_info(a, b=[]):
        print(b)
        return b
    result = print_info(1)
    result.append('error')
    print_info(2)

    # 上面的方式, 再次调用函数,返回的值会是改变后的默认参数的值 , 如果传入的默认参数是可修改的(对象指向不变，所以值会被更改),必须在函数中新建一个对象返回出去。
    def print_info1(a, b=None):
        print('in info1:%s'%b)
        if b is None:
            b = []
        return b;
    result = print_info1(1)
    result.append('error')
    print_info1(2)

def moduleDemo():
    """
    导入模块
        三种方式导入:
        1、import 模块名
        2. form 模块名 import 属性/方法   : 导入模块中的属性和方法  from sys import version
        3. form 模块名 import *  : 导入模块中的所有属性和方法
    :return:
    """
    import sys
    from sys import version
    print(sys.version)
    print("form version:%s"%version)

def classDemo():

    """
    新式类 继承时 广度优先 ，就是从上一级从左往右继承
    :return:
    """
    class A1():
        def run(self):
            print('A1')

    class A2():
        def run(self):
            print('A1')
            
    class Animal(A1,A2):
        # def run(self):
        #     print('animal')
        pass

    class Plant():
        def run(self):
            print('plant')

    class A(Animal,Plant):
        pass
    a =A()
    a.run()

    class Dog(name):
        def run(self):
            pass


classDemo()
moduleDemo()
funcDemo()
lambdaDemo()
ifDemo()
dicDemo()
setDemo()

