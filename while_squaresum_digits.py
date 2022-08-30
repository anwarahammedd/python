#Find the sum of digits square
#3  3*3 + 2*2 + 1*1 = 14
n=int(input("Enter a Number:"))
sum=0
while(n>0):
    d=n%10
    n=n//10
    sum=sum+d**2
print(sum)
