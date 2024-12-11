def calc():
    print("this a simple calculator")
    print(" 1 addition/n 2 subtraction/n 3 division/n 4 mulitiplocation")
    choice = eval(input("choose your operation"))
    num1 = eval(input("enter your first number"))
    num2 = eval(input("enter your second number"))

    if choice == 1:
        print(f" the answer is {num1 + num2}")
    elif choice == 2:
        print(f"the answer is {num1 - num2}")
    elif choice == 3:
        if num2 == 0:
            print("cannot divide by 0")
        else:
            print(f"the answer is {num1 / num2}")
    elif choice == 4:
        print(f"the answer is {num1 * num2}")
    else:
        print("invalid choice")


calc()
