# # 列表生成式
c=(i*2 for i  in range(10))
print(c)
print(c.__next__())


#
#斐波那契
def fib(max):
    n,a,b=0,0,1
    while n<max:
        # print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

c=fib(10)
print(c.__next__())

while True:
    try:
        print(c.__next__())
    except StopIteration as e:
        print("exception:",e.value)
        break


# 例子

import  time
def consumer (name):
    print("%s准备吃包子啦！"%name)
    while True:
        baozi=yield
        print("包子[%s]来了,被[%s]吃了！"%(baozi,name))

c=consumer("domain")
c.__next__()
c.send("韭菜馅")


def producer ():
    c1=consumer("domain")
    c2=consumer("alex")
    c1.__next__()
    c2.__next__()
    print("开始做包子")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子",i)
        c1.send(i)
        c2.send(i)
producer()




