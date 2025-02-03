"""Q1.
Ask a number from user. Print
Even
or
Odd."""

num = int(input("enter the number "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

"""Q2.
Ask a number from user. Print
Positive, Negative or Zero.
"""
num = int(input("enter the number "))

if num <= 0:
    if num == 0:
        print("Zero")
    else:
        print("Negative")
else:
    print("positive")


"""Q3.
Ask a number from user. Print
Yes
if the number is divisible by 2,3 and 5.
"""
num = int(input("enter the number "))

if num%2==0 and num%3==0 and num%5==0:
    print("Yes")
else:
    print("No")


"""Q4.
Write a Python program that accepts an integer number from the user and classifi es it as:
Positive and Even
Positive and Odd
Negative and Even
Negative and Odd
Zero

Input
: An integer (e.g., -4)
Output
: Negative and Even
"""

num = int(input("enter the number "))

if num%2 == 0 and num > 0:
    print("Positive and Even")
elif num%2 != 0 and num > 0:
    print("Positive and odd")
elif num%2 == 0 and num < 0:
    print("Negative and Even")
elif num%2 != 0 and num < 0:
    print("Negative and odd")
else:
    print("Zero")

"""Q5.
Write a Python program that accepts a student's marks in three subjects and prints the grade based on the following conditions:
Marks > 90: Grade A
80 < Marks <= 90: Grade B
70 < Marks <= 80: Grade C
60 < Marks <= 70: Grade D
Marks <= 60: Fail

Input
: Three integer marks (e.g., 85, 92, 78)
Output
: Grade B
"""

sub1 = int(input("enter the sub1 marks : "))
sub2 = int(input("enter the sub2 marks : "))
sub3 = int(input("enter the sub3 marks : "))

Marks = (sub1 + sub2 + sub3)//3
print(f"Total marks in % {Marks}")

if Marks > 90:
    print("Grade A")
elif 80 < Marks <= 90:
    print("Grade B")
elif 70 < Marks <= 80:
    print("Grade C")
elif 60 < Marks <= 70:
    print("Grade D")
else:
    print("Fail")


"""
Q6.
Write a program to find the maximum and minimum of three numbers entered by the user using if-else statements.
Input
: Three integers (e.g., 3, 9, 5)
Output
: Max is 9 and Min is 3
"""
num1 = int(input("Enter the num1 "))
num2 = int(input("Enter the num2 "))
num3 = int(input("Enter the num3 "))

# Finding the maximum number using if-else
if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

# Finding the minimum number using if-else
if num1 <= num2 and num1 <= num3:
    minimum = num1
elif num2 <= num1 and num2 <= num3:
    minimum = num2
else:
    minimum = num3

# Displaying the result
print(f"Max is {maximum} and Min is {minimum}")

"""
Q7.
Write a Python program that calculates the BMI and classifi es it based on the following conditions:
BMI < 18.5: Underweight
18.5 <= BMI < 24.9: Normal weight
25 <= BMI < 29.9: Overweight
BMI >= 30: Obesity
BMI is calculated as weight(kg) / height(m)^2
Input
: Weight in kg and Height in meters (e.g., 70, 1.75)
Output
: Normal weight
"""

# Get weight and height from the user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Classify BMI
if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi < 24.9:
    classification = "Normal weight"
elif 25 <= bmi < 29.9:
    classification = "Overweight"
else:
    classification = "Obesity"

# Display result
print(f"BMI: {bmi:.2f}, Classification: {classification}")



"""Q8.
Write a Python program to determine if a student is eligible for college admission based on the following criteria:

Minimum score in Math: 70
Minimum score in Science: 65
Minimum score in English: 60
Total score across all subjects: 200

Input
: Three scores (e.g., 75, 70, 65)
Output
: Eligible for Admission"""

# Get scores from the user
math_score = int(input("Enter Math score: "))
science_score = int(input("Enter Science score: "))
english_score = int(input("Enter English score: "))

# Checking individual subject criteria
if math_score >= 70 and science_score >= 65 and english_score >= 60:
    total_score = math_score + science_score + english_score
    if total_score >= 200:
        print("Student is eligible for college admission.")
    else:
        print("Student is not eligible: Total score is below 200.")
else:
    print("Student is not eligible: Does not meet minimum subject requirements.")