# 三级菜单

data={
    "江西省":{
        "赣州市":{
            "于都县",
            "会昌县",
            "龙南县",
            "安远县"
        },
        "南昌市": {
            "西湖区",
            "东湖区",

        },

    },

    "福建省": {
        "福州市": {
            "鼓楼区",
            "台江区",
            "仓山区",
            "马尾区"
        },
        "厦门市": {
            "思明区",
            "集美区",

        },

    },
}





while True:
    for item in data:
        print(item)
    choice =input("选择进入市,输入q 退出:")
    if choice in data:
        while True:
            for item2 in data[choice]:
                print(item2)
            choice2 = input("选择进入区县，输入b返回,输入q 退出:")
            if choice2 in data[choice]:
                while True:
                    for item3 in data[choice][choice2]:
                        print(item3)
                    choice3 = input("最后一层，输入b返回,输入q 退出:")
                    if choice3 =="b":
                        break
                    elif choice3 == "q":
                        exit()
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit()
    elif choice == "q":
        exit()