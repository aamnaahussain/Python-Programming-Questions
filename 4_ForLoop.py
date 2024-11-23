#CODE DOCUMENT-4

# 1. Print Numbers from 1 to 50
for i in range(50):
    print(i)

# 2. Print the sum of first 100 Natural Numbers
tsum=0
for i in range(1,101):
    tsum=tsum+i
print(tsum)


# 3. Multiplication Table
num=int(input("Enter the number for multiplication:"))
a1=num*11
count=0
for i in range(0,a1,num):
  print(num,"*",count,"=",count*num)
  count=count+1

# 4. Factorial Calculation
num4=int(input("Enter a number: "))
fac=1
for ele in range(num4,0,-1):
   fac=fac*ele
print("The factorial of ",num4," is ",fac)

# 5. Reverse a String
string5=input("Enter a string: ")
reversed_string=""
for char in string5:
   reversed_string= char + reversed_string
print("Original String: ",string5)
print("Reversed String: ",reversed_string) 

# 6. Find Prime Numbers in a Range
lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))

for num in range(lower,upper+1):
   if num>1:
      for i in range(2,num):
         if num%i==0:
            break;
      else:
            print(num)

# 7. Fibonacci Series 
num7=int(input("Enter a number: "))
x=0
y=1
z=0
for i in range(0,num7+1):
 if(z<=num7):
   print(z)
   x=y
   y=z
   z=x+y

# 8. Sum of Digits In List
list8=[2,4,6,8]
sum=0
for i in list8:
   sum=sum+i
print("The sum of list: ", list8 ," is ",sum)
    
# 9. Count Vowels in a String
string9=input("Enter a string: ")
vowels="AEIOUaeiou"
count=0
for char in string9:
   if char in vowels:
    count+=1
print("There are ",count," vowels in the string")


# 10. Average Of List
list11=[2,4,6,8]
length=len(list11)
sum=0
for ele in list11:
   sum=sum+ele
average=sum/length
print("The average of list: ",list11," is ",average)
     
# 11. UpperCase Letter In String
string12=input("Enter a string: ")
s12=""
count12=0
for char in string12:
   if char.isupper():
      s12=s12+char
      count12+=1
print("There are ",count12," uppercase letters which are: ",s12)

# 12. Print Largest Number In List
list13=[2,3,6,7,9]
largest_num=0
for element in list13:
   if(element>largest_num):
      largest_num=element
print("The largest number in the list: ",list13," is ",largest_num)
      


# 13. Print Reverse Numbers from 10 to 1
for i in range(10,-1,-1):
   print(i)

