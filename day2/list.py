# 2018年1月25日21:14:17  列表的使用



names=["domain","ZhanSan","LiSi","WanWu","WuDi","LiYiFeng","WuYiFang"]



# 增
names.append("domain")          # 在后面追加
names.insert(2,"insertZhan")    # 指定位置插入

print(names)

# 删
names.remove("domain")          # 指定值删除
names.pop(1)                    # 指定位置删除

print(names)

#查
print(names[2])                 #指定位置查询
print(names.index("domain"))           #指定位置查询

#切片
print(names[-3:])               #查询倒数第三个 至 最后一个
print(names[:3])                #查询第一个 至 第三个

print(names[1:3])               #查询第二个到第四个（不包括第四个）

print(names[1:5:2])             #步长切片，参数：起始位置，结束位置，步长





#改

names[2]="domain"               #指定位置更改

print(names)


# 其他方法
print(names.count("domain"))           #查询指定值的数量

names2=names.copy()             #拷贝列表   (浅拷贝：只拷贝第一层，独立拷贝第一层，如果列表里面有列表，则不会拷贝值，拷贝的是内存地址，更改原列表后，拷贝的列表也会变)
                                #（如何完全拷贝，深拷贝：导入copy库，用deepcopy 方法。则会完全克隆两份地址内存不一样的列表）
print(names2)


names.extend(names2)            #列表合并
print(names)

names.reverse()                 #列表顺序反转
print(names)

names.sort()                    #列表排序
print(names)

names.sort()

print("排序后:",names)


names.clear()                   #列表元素清除
print(names)

del names2                      #清除（删除全部，包括列表名）列表
list = ["domain"]
list1 = ["domain"]
for i  in  range(3):


    list.append(list1)
print("---",list)




