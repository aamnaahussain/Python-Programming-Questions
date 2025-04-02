#CODE DOCUMENT-1, Operators

#Question-1:
print("Question-1:")
print("Enter two numbers such that Number 1 is greater than Number 2")
a1=int(input("Enter the first number:"))
a2=int(input("Enter the second number:"))

if (a1>a2):
    print(True)
else:
    print(False)

#Question-2:
print("\nQuestion 2  - Even Number Check")
a2=int(input("Enter a number:"))
if a2%2==0:
    print("The number is even")
else:
    print("The number is odd")

#Write a program that checks whether a given temperature is within a safe range
print("\nQuestion 3  - Temperature Range")
def temp_check(temp):
    if 15<=temp<=25:
        print("Safer Temperature")
    else:
        print("Not Safer Temperature")
    

temp_check(13)



# Create a function that takes two Boolean values as input. 
# Return True if both values are True (using the and operator), and return False if one or both values are False.
# Then modify the function to return True if either of the values is True (using the or operator).
print("\nQuestion 4  - Boolean Operators")
def and_operation(val1,val2):
    return val1 and val2

def or_operation(val1,val2):
    return val1 or val2


print("For AND Operation:")
print(and_operation(True,False))

print("For OR Operation:")
print(or_operation(True,False))


#Question-4: Increment and Decrement a Number
print("\nQuestion 4  - Increment and Decrement a Number\b")
a4=int(input("Enter a number: "))

print("After Increment:")
inc=a4+1
print(inc)
result=inc-2

print("Final Result:")
print(result)