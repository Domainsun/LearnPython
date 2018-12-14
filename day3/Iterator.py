from collections import  Iterable,Iterator
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({"name","domain"},Iterator))
print(isinstance("domain",Iterator))
print(isinstance(123,Iterator))

a=[1,2,3]
b=iter(a)
b.__next__()

for x in range(10):
    print(x)

it = iter([0,1,2,3,4,5,6,7,8,9])
while True:
    try:
        x=it.__next__()
        print(x)
    except:
        break

f=open("hello","r+",encoding="utf-8");
f.write("hello\n")
f.write("hello\n")
f.write("hello\n")
f.write("hello\n")
f.write("hello\n")

for f in f:
    print(f)

