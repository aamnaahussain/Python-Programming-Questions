#CODE DOCUMENT-2

#1. Reverse String
print("Question 1 - Reverse String")
x=input("Enter a string:")
y=x[-1::-1]
print("The reverse of the string is:",y)


#2. Palindrome Check
print("Question 2 - Palindrome Check")
a=input("Enter a string:")
b=a[-1::-1]

if(a==b):
    print("The entered string is Palindromic")
else:
    print("The entered string is not Palindromic")

#3. String Concatenation
print("Question 3 - String Concatenation")
e="Amna "
f="Hussain"
ans1= e+f
print(ans1)

#4. Write a Python function to check if one string is a rotation of another string.
print("Question 4 - Rotation Check")
g="abcde"
h="cdeab"

def stringrotation(str1,str2):
    if(len(str1) != len(str2)):
        return False
    return str2 in (str1+str1)

print(stringrotation(g,h))

#5.Write a function that checks if two given strings are anagrams of each other.
print("Question 5 - Anagrams Check")
i="silent"
j="listen"
#An anagram is when two strings have the same characters with the same frequency, but arranged in a different order.
def anagram_check(str1,str2):
    return sorted(str1) == sorted(str2)
        
print(anagram_check(i,j))

#6. Count Words in a String
print("Question 6 - Count Words in a String")
k="-My name is Amna-"
def word_count(str1):
    return len(str1.split())

print("With the string ",k," -",word_count(k))
    


#7. Check if String Contains Only Digit9
print("Question 7 - String Contains Only Digit")
m="1234"
n="12s34"  

def onlydigit(str1):
    return str1.isdigit()

print("With the string ",m," -",onlydigit(m))
print("With the string ",n," -",onlydigit(n))