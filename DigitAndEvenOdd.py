x = (input("Enter: "))

if x.isdigit():
    x_num = int(x)
    if (x_num % 2) == 0:
        print("It is an Even Number")
    else:
        print("It is an Odd Number")
else:
    print("It is Not A number")
