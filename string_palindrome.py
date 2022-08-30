#check given number palindrome or not

#str=input("Enter a string")
#str1=str[::-1]
#print(str1)
#f(str1==str):
#    print("It is Palindrome")
#else:
#    print("It is not Palindrome")

n=int(input("Enter a Number:"))
str1=str(n)
str2=str1[::-1]
if(str1==str2):
    print("Palindrome")
else:
    print("Not Palindrome")
