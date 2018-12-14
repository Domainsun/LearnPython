name = "d\tomainaaa"
print("首字母大写后：", name.capitalize())  # 给字符串的首字母大小
print("a总共有{_count}个".format(_count=name.count("a")))# 找出字符串中指定字符的个数
print("居中显示，50个字符，不足补-:", name.center(50, "-"))#给字符串设置长度并居中显示，不足用指定的字符补足
print("居左显示，50个字符，不足补*:", name.ljust(50, "*"))#给字符串设置长度并左显示，不足用指定的字符补足
print("居右显示，50个字符，不足补+:", name.rjust(50, "+"))#给字符串设置长度并右显示，不足用指定的字符补足
print("是否aaa结尾:", name.endswith("aaa"))#判断字符串是否是指定的字符结尾
print("给tab 空20个字符:", name.expandtabs(tabsize=20))#给字符串中的tab 设置大小
print("索引main的起始位置:", name.find("main")) #找到指定字符的起始位置
print("是否为字母数字组合:", name.isalnum()) #判断字符串是否为字母和数组的组合
print("是否为纯英文字符:", name.isalpha())  # 判断字符串是否为英文字符
print("1A是否为十进制:", "1A".isdecimal())  # 判断字符串是否为十进制
print("1A是否为整数:", "1A".isdigit())  # 判断字符串是否为整数
print("1A是否为合法的变量名:", "1A".isidentifier())  # 判断字符串是否为合法变量名
print("1A是否为数字:", "1A".isnumeric())  # 判断字符串是否为数字
print("1A是否为空格:", "1A".isprintable())  # 判断字符串是否为空格
print("Is Me 是不是标题:", "Is Me".istitle())  # 判断字符串是否是标题
print("Is Me是否能被打印", "Is Me".isprintable())  # 判断字符串是否能被打印
print("IME是不是大写", "IME".isupper())  # 判断字符串是否为大写
print("123加分隔符+", '+'.join(['1', '2', '3']))  # 列表加上指定分隔符变成字符串
print("Domain转小写", "".lower())  # 字符串转小写
print("domain转大写", "".upper())  # 字符串转大写
print("   移除左边空格".lstrip())  # 移除字符串左边空格
print("移除右边空格   ".rstrip())  # 移除字符串右边空格
print("移   除 所有 空格   ".strip())  # 移除字符串所有 空格
p = str.maketrans("0987612345", 'abcdefgoti')  # 产出一个对应值的翻译
print("73 54".translate(p))  # 输入上面定义好的对应的值：输出 do it
print("domaind".replace('d', 'a', 1))  # 把字符串中指定值替换成其他指定的值，第三个参数为替换的个数
print("domaind".rfind('d'))  # 找到指定字符在最右边的索引
print("1-2-3-4-5".split('-'))  # 以指定的分隔符把字符串分割成列表
print("domainABcE".swapcase())  # 把字符串中的大写变小写，小写变大写
