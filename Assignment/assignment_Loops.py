"""
Q1.
Ask a positive number from user. Print from
1 to n.
"""
n = int(input("Enter the number : "))

i = 1
while i <= n:
    print(i,end=" ")
    i += 1

"""Q2.
Ask a positive number from user. Calculate the total sum of all the numbers from
1 to n."""

n = int(input("Enter the number : "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)

"""Ask a start number and end number from user. Calculate the total sum of all the numbers from
start to end."""

s = int(input("Enter the start number : "))
e = int(input("Enter the end number : "))

i = s

sum = 0

while i <= e:
    sum = sum + i
    i += 1
print(sum)

"""Ask a positive number from user. Print from
n to 1."""

n = int(input("Enter the number : "))

i = 1

while n >= i:
    print(n,end= " ")
    n -= 1

"""Ask a positive number from user. Print from
n to -n."""

n = int(input("Enter the number : "))

i = -n

while n >= i:
    print(n,end=" ")
    n -= 1

"""Print all the numbers divisible by 2, 3 and 5 from
start to end.
Ask start and end numbers from the user."""

start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

i = start

while  i <= end:
    if i%2 ==0 and i%3 == 0 and i%5 == 0:
        print(i, end= " ")
    i += 1

"""Ask a number from user. Print the multiplication table of that number."""

n = int(input("Enter the number : "))

i = 1

while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1

"""Ask a start number and end number from user. Ask another number n
from the user. Print all the numbers from start to end divisible by n."""

start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

n = int(input("Enter the number : "))

i = start

while i <= end:
    if i % n == 0:
        print(i,end=" ")
    i += 1

"""Q9.
Count the number of odd and even numbers from
start to end.
Ask start and end number from user."""

start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

i = start

odd_count = 0
even_count = 0

while i<= end:
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1

    i += 1

print(f"Even_count {even_count}")
print(f"Odd_count {odd_count}")

"""Q10.
Ask two number from user that is start and end. Also start can be greater or smaller than the end number.
Print from start to end. See the examples below.
Example 1:
Enter start = 5
Enter end = 10
Output:
5 6 7 8 9 10
"""

start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))

i = start

if start <= end:
    while i <= end:
        print(i, end=" ")
        i += 1
else:
    while i >= end:
        print(i, end=" ")
        i -= 1


"""Q11.
Print the following pattern. Ask n from user.
Example 1:
Enter n = 6
Output:
1 2 4 8 16 32"""


n = int(input("Enter the number : "))

i = 0

while i < n:
    print(2 ** i,end=" ")
    i += 1

"""Q12.
Print the following pattern. Ask n from user.
Example 1:
Enter n = 5
Output:
1 11 111 1111 11111"""

n = int(input("Enter the number: "))

i = 1
while i <= n:
    print(int("1" * i), end = " ")
    i += 1