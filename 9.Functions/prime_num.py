"""
Ask a integer as a parameter
Return True if that number is prime else print False

"""

def prime(num:int)->bool:
    if num > 1:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                return "False"
                break
        else:
            return "True"
    else:
        return "False"

num = int(input("Enter the number "))
print(prime(num))

#=====

def check_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter the number "))
print(check_prime(num))
