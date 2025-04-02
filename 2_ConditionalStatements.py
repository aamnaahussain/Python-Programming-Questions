#CODE DOCUMENT-3, Conditional Statements

#1. Leap Year Check
year = int(input("Enter the year:"))

if (year%4 == 0  and  year%100 != 0) or (year%400 == 0):
    print("The year ",year," is a leap year")
else:
     print("The year ",year," is not a leap year")
# A year is a leap year if:
# It can be divided by 4 (year % 4 == 0).
# But if the year is also divisible by 100 (century years like 1900, 1800):
# It must also be divisible by 400 (year % 400 == 0).
# If it’s divisible by 100 but not by 400, it is not a leap year

#2. Number Comparison
num1=int(input("Enter the first number:"))
num2=int(input("Enter the first number:"))
if(num1>num2):
    print(num1," is greater than ",num2)
elif(num1<num2):
    print(num2," is greater than ",num1)
else:
    print(num2," is equal to ",num1)

#3. Even or Odd
num3=int(input("Enter the first number:"))
if(num3%2==0):
    print("The number ",num3," is even")
else:
    print("The number is odd")

#4. Positive/Negative/Zero
num5=int(input("Enter the first number:"))
if(num5>0):
    print(" The number entered is positive ")
elif(num5<0):
    print(" The number entered is negative")
else:
    print("The number entered is Zero ")

#5. Grading System
num6=int(input("Enter marks:"))
if(50<=num6<=60):
    print("Your Grade is D")
elif(num6<49):
    print("You are fail, Grade is F")
elif(60<=num6<=70):
    print("Your Grade is C")
elif(70<=num6<=80):
    print("Your Grade is B")
elif(80<=num6<=90):
    print("Your Grade is A")
elif(90<=num6<=100):
    print("Your Grade is A+")
else:
    print("the number entered is incorrect\nEnter number less than 100")

#6. Traffic Light System Simulation
color = input("Enter a traffic light color (red, yellow, green):\n").lower()

if color == "red":
    print("Stop")
elif color =="yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")

#7. BMI Calculator
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your hieght in meters:"))
bmi=weight/(height**2)
print("Your bmi is ",bmi)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi <=24.9:
    print("your weight is normal")
elif 25 <= bmi <= 29.9:
       print("You are over weight")
else:
    print("You are obese")

#8. Vowel or Consonant
alphabet = input("Enter an alphabet:\n")
if alphabet in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
    print("It's a vowel")
else:
    print("It's a consonant") 