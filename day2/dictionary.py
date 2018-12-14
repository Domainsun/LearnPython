# key-value

# 字典是无序的

# 定义
info = {
    "name": "domain",
    "age": 15,
    "job": "IT",
    "future": "cool"
}

# 增
info["sex"] = "male"  # 新增一个 key-value

# 删
del info["job"]  # 删除指定key的键值对
info.pop("name")  # 删除指定key的键值对
info.popitem()  # 随机删除键值对

# 查

info["future"]  # 如果不存在，报错
info.get("age1")  # 如果不存在，返回none

print("age1" in info)  # 判断字典中是否有key为age1的键值对

# 改
info["sex"] = "female"  # 改变指定key的值

print(info)

# 多级嵌套

book = {

    "science":
        {
            "三体": ["大型科幻小说", 158],
            "盗墓笔记": ["古代盗墓故事", 178],
            "鬼吹灯": ["惊悚鬼故事", 58]
        },

    "romance":
        {
            "霸道总裁爱上我": ["大型科幻小说", 158],
            "霸道总裁爱上我2": ["大型科幻小说", 158],
            "霸道总裁爱上我3": ["大型科幻小说", 158],
        },

    "prose":
        {
            "草房子": ["曹文轩散文书籍", 58],
            "草房子2": ["曹文轩散文书籍", 58],
            "草房子3": ["曹文轩散文书籍", 58],
            "草房子4": ["曹文轩散文书籍", 58],
        },
}

print(book)

# 其他方法

book.values()  # 得到典所有value
book.keys()  # 得到字典所有value

book.setdefault("game", {"英雄联盟": ["大型网络游戏", 99999999999]})  # 添加一个键值对，有则不再添加，无则添加

print(book)




pass_through = {                                                        #新建一个字典

    "pass_through":
        {
        "crossfire": ["大型网络游戏穿越火线", 99999999999]
    },
    "prose":
        {
            "草房子": ["曹文轩散文书籍", 58],
            "丫头": ["网络电视剧原小说", 58],
            "草房子2": ["曹文轩散文书籍", 58],
            "草房子3": ["曹文轩散文书籍", 58],
        }
}

book.update(pass_through)                                       #把刚刚新建的字典更新到之前的book字典，重复的不更新，不重复的加上
print(book)

print(book.items())          #字典转列表

c=dict.fromkeys(["name1","name2","name4"],["domain","marry","alex"])  #新建一个字典，第一个参数是所有的key,第二个参数是所有key的value，ps:改变其中一个key的value，如果value有两层，那么所有key的value都会改变，同列表的浅拷贝
print(c)


# 循环
print("循环方式一".center(30,"-"))
for i in book:
    print(i,book[i])

print("循环方式二".center(30,"-"))   #比上面方式低效，要先转成列表，如果数据量大，运行速度会变慢
for k,v in book.items():
    print(k,v)







