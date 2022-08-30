#How to count Numbers in a string
#str=34reffdr5656dfds

str=input("Enter a String:")
str2=str.lower()
num=0
vowel=0
space=0
cons=0
for i in str2:
    if i in '1234567890':
       num=num+1
    elif i=='aeiou':
       vowel+=1
    elif i==' ':
       space+=1
    else:
       cons+=1
print("No. of Numbers:",num)
print("No. of Vowels:",vowel)
print("No. of Space:",space)
print("No. of Constants:",cons)


