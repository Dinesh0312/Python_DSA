# Exception Handling
try:
    n = 10
    result = n/int(input("Enter the number "))  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print(f"A digit {n} can not be devide by Zero")
else:
    print("Result is", result)
finally:
    print("Execution complete.")
