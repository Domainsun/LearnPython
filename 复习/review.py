# coding=gbk
def setDemo():
    """

    """

    set1 = set([1, 2, 1, 1, 13, 4, 111])
    print(set1)


def dicDemo():
    '''
    �ֵ�(dict)����ʾ��
    ע��:
        1.�����ظ�key�����ظ�key ʱ, ����֮ǰ�ĵ�key,value�������һ�θ�ֵΪ׼
        2.����
        3.key���ɱ䣬����key���������֣��ַ�����Ԫ��䵱�����Ǿ��ǲ���ʹ���б�
        4.value����Ϊ��������

    �����ͺ���	����
        cmp(dict1, dict2)	�Ƚ������ֵ�Ԫ��
        len(dict)	�����ֵ�Ԫ�ظ���
        str(dict)	����ֵ�ɴ�ӡ���ַ�����ʾ
        type(variable)	��������ı������ͣ�����������ֵ�ͷ����ֵ�����
        dict.clear()	ɾ���ֵ�������Ԫ��
        dict.copy()	����һ���ֵ��ǳ����
        dict.values()	���б����ֵ��е�����ֵ
        popitem()	������ز�ɾ���ֵ��е�һ�Լ���ֵ
        dict.items()	���б��ؿɱ�����(��, ֵ) Ԫ������
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
    if num:  # ������ֵ���ǿ��ַ������ǿ� list �ȣ��ж�ΪTrue������ΪFalse
        print('hello world')
    java = 86
    python = 68

    if java > 80 and python > 80:
        print('����')
    else:
        print('������')

    if (java >= 80 and java < 90) or (python >= 80 and python < 90):
        print('����')

def lambdaDemo():
    """
    lambda :��������

    :return:
    """          #:ǰ�Ǵ���Ĳ���, :���Ǳ��ʽ,����ֵΪ���ʽ�ļ���ֵ
    sum = lambda num1, num2: num1 + num2+3;
    print(sum(1, 2))

def funcDemo():
    """
    �� Python �У��ַ��������Σ������ͣ�tuple �ǲ��ɸ��ĵĶ��󣬶� list �� dict ���ǿ��Ը��ĵĶ���
    ���ɸ��ĵ����ͣ�
        ������ֵ a = 1����ʵ��������һ�����ζ��� 1 ��Ȼ����� a ָ�� 1���� a = 1000 ��ʵ����������һ�����ζ��� 1000��Ȼ��ı� a ��ָ�򣬲���ָ�����ζ��� 1 ������ָ�� 1000����� 1 �ᱻ����
    �ɸ��ĵ����ͣ�
        ������ֵ a = [1,2,3,4,5,6] ����������һ������ list ��list ������ 6 ��Ԫ�أ������� a ָ�� list ��a[2] = 5���ǽ� list a �ĵ�����Ԫ��ֵ����,����������ǲ�ͬ�ģ������ǽ� a ����ָ�򣬶���ֱ���޸� list �е�Ԫ��ֵ��
    :return:
    """
    def print_info(a, b=[]):
        print(b)
        return b
    result = print_info(1)
    result.append('error')
    print_info(2)

    # ����ķ�ʽ, �ٴε��ú���,���ص�ֵ���Ǹı���Ĭ�ϲ�����ֵ , ��������Ĭ�ϲ����ǿ��޸ĵ�(����ָ�򲻱䣬����ֵ�ᱻ����),�����ں������½�һ�����󷵻س�ȥ��
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
    ����ģ��
        ���ַ�ʽ����:
        1��import ģ����
        2. form ģ���� import ����/����   : ����ģ���е����Ժͷ���  from sys import version
        3. form ģ���� import *  : ����ģ���е��������Ժͷ���
    :return:
    """
    import sys
    from sys import version
    print(sys.version)
    print("form version:%s"%version)

def classDemo():

    """
    ��ʽ�� �̳�ʱ ������� �����Ǵ���һ���������Ҽ̳�
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

