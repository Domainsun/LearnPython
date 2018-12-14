for thief in ['a','b','c','d']:

    # print(thief!='a')
    sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief !='d')
    print(sum)
    if sum == 3:
        print("小偷是：%s " % thief)
