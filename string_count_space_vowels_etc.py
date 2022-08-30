#input string
#count vowels, space, consonents

str=input("Enter the string")
str2=str.lower()
vowel=0
space=0
con=0
for i in str2:
    if i in 'aeiou':
       vowel+=1
    elif i==' ':
        space=space+1
    else:
        con=con+1
print("Number of vowel:",vowel)
print("Number of space:",space)
print("Number of constant:",con)