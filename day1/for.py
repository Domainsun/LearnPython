myAge = 16

count = 0
while count < 3:
    age = int(input("guess my age:"))
    if age == myAge:
        print("yes, you got it!")
        break
    elif age < myAge:
        print("think bigger...")
    elif age > myAge:
        print("think smaller...")

    count += 1
    if count == 3:
        confirm = input("do you want keep trying? input n/y")
        if confirm == 'y':
            count = 0
        else:
            print("you already exit.")
