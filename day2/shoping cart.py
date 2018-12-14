goods = [["Milk Tea", 12], ["Coffee", 68], ["Ice Cream", 30], ["Bread", 15]]
shoplist = []
salary = input("Please input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(goods):  # 用enumerate方法拿出下标
            print(index, item[0], item[1])
        user_choice = input("Please choice goods")
        if user_choice.isdigit():  # 判断是不是数字
            user_choice = int(user_choice)
            if user_choice >= 0 and user_choice < len(goods):  # 判断是否小于列表的长度
                if salary >= goods[user_choice][1]:  # 判断余额是否大于商品价格
                    salary -= goods[user_choice][1]  # 减去选择商品的价格，得出余额
                    shoplist.append(goods[user_choice])  # 添加选择进购物车
                    print("You have buyed ")
                    for index, item in enumerate(shoplist):  # 用enumerate方法拿出下标
                        print(item[0], )
                    print("and your balance is ", salary)
                else:
                    print("Your balance is not enough!")

            else:
                print("This option is not exsit!")
        elif user_choice == 'q':  # 输入  q  退出
            exit("You have quit.")
        else:
            print("Invalid option!")
else:
    print("Please input number!")
