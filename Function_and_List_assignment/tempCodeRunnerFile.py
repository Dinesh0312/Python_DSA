def check_number(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter the number = "))

check_number(num)