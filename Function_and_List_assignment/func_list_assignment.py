"""
Q1. Write a function named celsius_to_fahrenheit that converts Celsius to
Fahrenheit and prints the result. (Formula: (Celsius * 9/5) + 32 = Fahrenheit)

"""

def celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9/5) + 32
    return Fahrenheit

celsius = int(input("Enter the celsius to convert into Fahrenheit = "))

print(celsius_to_fahrenheit(celsius))

"""
Q2. Create a function named simple_calculator that takes three
parameters: two numbers and an operation (addition or subtraction
represented by '+' or '-'), and prints the result of the operation.

"""

def simple_calculator(a,b,c):
    if c == '+':
        addition = a + b
        print(addition)
    elif c == '-':
        subtraction = a - b
        print(subtraction)
    else:
        print("Invalid operator")

a = int(input("Enter a numbe a = "))
b = int(input("Enter a numbe b = "))
c = input("Enter a operator to perform = ")

simple_calculator(a,b,c)

"""
Q3. Write a function named check_number that takes a number and prints
whether it is positive, negative, or zero.
"""

def check_number(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter the number = "))

check_number(num)


"""
Q4. Write a function named is_odd_even that determines if a number is
odd or even without using the modulo operator (%). Hint: Use division or
subtraction.
"""

def is_odd_even(number: int):
    if (number // 2) * 2 == number:
        print("Even")
    else:
        print("Odd")


is_odd_even(2)
is_odd_even(3)

"""
Q6. Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1.

"""

# Without Annotations
def largest(num1=None, num2=None, num3=None) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1

print(largest(3, 4, 1))