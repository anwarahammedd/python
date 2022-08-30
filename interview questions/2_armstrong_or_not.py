#Check the given number is amstrong or not
n=int(input("Enter a number:"))
num=n
sum=0
while(n>0):
    d=n%10
    n=n//10
    sum=sum+d**3
if(sum==num):
    print("Given Number is Amstrong")
else:
    print("Given Number is not Amstrong")
