"""Q1.
Factorial of a Number: Write a program to calculate the factorial of a
given number using a loop."""

n = int(input("Enter the number : "))

fact = 1

for i in range(1,n+1):
    fact = fact * i
print(fact)


"""Q2.
Ask a number from user. Print all the factors of a that number. (Order does not matter, just print it)"""

n = int(input("Enter the number : "))

for i in range(1,n+1):
    if n%i==0:
        print(i)

"""Q3.
Ask a number from user. Count the number of factors of that number."""

n = int(input("Enter the number : "))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count += 1
print(count)

"""Q4.
Ask a number from user. Print the sum of all the factors of that number."""

n = int(input("Enter the number : "))
sum = 0

for i in range(1,n+1):
    if n%i==0:
        sum = sum + i
print(sum)

"""Q5.
Ask a number from user. Print Yes if that number is a prime number else print No"""

n = int(input("Enter the number : "))

for i in range(2,(n//2)+1):
    if n%i==0:
        print("NO")
        break
else:
    print("Yes")

"""Q6.
Write a program to check if a given number is a perfect number.
A number is called perfect if it is equal to the sum of its proper divisors (divisors excluding the number itself).
Requirements:
Example Scenarios to Consider:
1. You are given a positive integer n (Ask from user)
2. Your task is to check if n is a perfect number or not using a loop.

Example Scenarios to Consider:
1.
Input : 6
Output : True
Explanation : The divisors of 6 are 1, 2, 3. The sum is 1 + 2 + 3 = 6, so it is a perfect number.
"""
n = int(input("Enter the number : "))
sum = 0

for i in range(1,(n//2)+1):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print("Its a perfect number")
else:
    print("Its not a perfect number")


"""
Q7.
Write a program to repeatedly sum the digits of a number until only a single-digit number is obtained.
The process involves summing the digits of the number and then repeating the process with the result until the number is reduced to a single digit.
Requirements:
1. You are given a positive integer n (Ask n from user)
2. You need to find the sum of the digits of n, and if the result is greater than 9, repeat the process.
3. Continue summing the digits until the result is a single-digit number.
4. Do not use lists, strings, dictionaries, or nested loops.

Example:
1.
Input : 9875
Output : 2
Explanation:
Step 1: 9 + 8 + 7 + 5 = 29
Step 2: 2 + 9 = 11
Step 3: 1 + 1 = 2 (single digit obtained).

"""

n = int(input("Enter a number = "))
while n >= 10:
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    n = sum_of_digits
print(n)