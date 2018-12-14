# #ps 字符串不能修改  eval
# # 数字转二进制
# print(bin(23))
# # 判断真假
# print(bool(0))
# # 字符转assc码
# a=bytearray("abcde",encoding="UTF-8");
# print(a[0])
#
# b=bytes("23232",encoding="UTF-8")
# print(b[0])
#
# #asscii 对应的数字转化成对应的字符
# print(chr(97))
# #asscii 对应的字符转化成对应的数字
# print(ord("a"))
#
# # 执行字符串代码
# exec("for i in range(10):print(i)")
#
# #
# # delattr()
#
# a={}
#
# print(dir(a))
#
# # 返回商和余数
# print(divmod(5,3))
#
# # eval()
#
# # res=lambda x:x+2,range(10)
# # # print(res)
# # for i in res:
# #     print(i)
#
# # 匿名函数
# (lambda x,y:print(x+y))(5,10)
#
# # 过滤大于5
res=filter(lambda x:x>5,range(10))
for i in res:
    print(i)
#
# # 生成列表
res=map(lambda x:x*x,range(10))
for i in res:
    print(i)

import functools
res=functools.reduce(lambda x,y:x*y,range(1,4))  #  1*2*3
print(res)

a=frozenset([1,2,3,4,5])

# 以字典形式返回当前文件所有全局变量，
print(globals())

#以字典形式返回当前文件所有局部变量，
locals()

print(max(2,3,4,4))

a=globals()
if "res" in a.keys():
    print("true")


#十六进制

print(hex(100))
print(oct(100))

print(ord('a'))


# a=[1,2,3]
# b=iter(a)
#
# print(reversed(b))
#取小数点五位
print(round(1.3333445,5))


a={1:3,3:2,4:6,7:4}

print(sorted(a.items()))  #按key 排序
print(sorted(a.items(),key=lambda x:x[1])) #按value 排序  x=每一个item项，x[1]就是指定的排序的key

def func(x):
    print(x[1])
func(a)

# 合并两个数据，返回一个个元组
a={'a','b','c','d'}
b={1,2,3,4}
res=zip(a,b)
for i in res:
    print(i)

#通过字符串 import 模块

__import__('decorator')
