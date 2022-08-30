#Reverse of a number
#123  321
n=int(input("Enter a Number:"))
s=0
while(n>0):
    d=n%10
    n=n//10
    s=s*10+d
print(s)