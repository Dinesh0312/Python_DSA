n = int(input("Enter the number : "))
sum = 0

for i in range(1,(n//2)+1):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print("Its a perfect number")
else:
    print("Its not a perfect number")