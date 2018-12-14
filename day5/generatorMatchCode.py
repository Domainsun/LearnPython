import  random
matchCode=''
for i in range(4):
    temp=''
    if random.randint(0,2)==random.randint(0,2):
        temp=chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    matchCode=matchCode+str(temp)
print(matchCode)