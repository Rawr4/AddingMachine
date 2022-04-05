while True:
    try:
        Num1 = int(input("Put a number"))
        Num2 = int(input("Put another number"))
        Sum = Num1 + Num2
        print(Sum)
        break
    except:
        print("Your input is not correct...")