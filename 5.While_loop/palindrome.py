num = int(input("Enter the number "))

n = num
ans = 0

while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n = n // 10
print(ans)

if num == ans:
    print("palindrome")
else:
    print("not palindrome")