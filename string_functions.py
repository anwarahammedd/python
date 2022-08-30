#find
#w1='i like python'
#r=w1.find('python')
#print(r)

#Read a string and a substring and print wheather the substring present in the string.
#i am very happy
#sad
#the substring is not present in the string
str1=input('Enter the string:')
substr=input('Enter the substring:')
r=str1.find(substr)
if(r!=-1):
    print("Presenet in the location",r)
else:
    print("Not Present in the string")

