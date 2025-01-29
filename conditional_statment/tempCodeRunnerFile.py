num = int(input("Enter the number: "))

if num%2 == 0 and num%3 == 0:
    print("FIZZBUZZ")
elif num%2 == 0:
    print("FIZZ")
elif num%3 == 0:
    print("BUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")