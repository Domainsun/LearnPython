import  re

# res=re.match('[a-zA-Z\_][0-9a-zA-Z\_]*','_a')
# print(res)



# match  ，从头匹配到第一个返回
#search  ，所有，匹配到第一个返回
#findall ，所有
#split   , 分割
#sub     ，替换

res=re.match(r'[a-z]+@[a-z]+.com', 'sunlongyue@foxmail.com')
print(res)