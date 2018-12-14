# decription: 兑换零钱：把总金额兑换成不同不固定面额不固定数量的硬币，得出兑换最少个数的方式。兑换不了返回-1
def exchange(list,amount):
    exchangelist = []
    last=len(list)-1
    for i,item in enumerate(list):
        merchant=(divmod(amount, item))[0]
        remainder=(divmod(amount, item))[1]
        print("商是%s,余数是%s"%(merchant,remainder))
        amount=remainder
        for j in range(int(merchant)):
            exchangelist.append(item)
        print("余额是%s"%amount)
        print("兑换方式%s"%exchangelist)
        if i==last:
            if amount!=0:
                return -1
            else:
                return exchangelist
a=[1,2.3,2]
list=exchange(sorted(a,reverse=True),11)
print("最后结果:",list)