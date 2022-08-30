#Write a program to reverse an integer
n=int(input("Enter the integer:"))
s=0
while(n>0):
    d=n%10
    n=n//10
    s=s*10+d
print("Reverse integer is:",s)
