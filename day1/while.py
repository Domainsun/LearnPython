myAge=16
count=0



# while count<3:
#     age = int(input("Guess my age:"))
#     if age<myAge:
#         print("think bigger...")
#     elif age>myAge:
#         print("Think smaller...")
#     elif age==myAge:
#         print("Yes, you got it.")
#         break
#     count=count+1
# else:
#     print("You have tried too many times!")
#

for i in  range(10):

    if i<5:
        continue
    print("loop:",i)

for i in range(10):
    print("loop",i)
    if i>5:
        break


while True:
    print("domain",count)
    count+=1
    if count==101:
        break


