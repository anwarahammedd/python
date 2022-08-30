#Check amstrong or not
#153

n=int(input("Enter a Number"))
sum=0
num=n
while(n>0):
        d=n%10
        n=n//10
        sum=sum+d**3
if(sum==num):
    print(sum,"is an Amstrong Number")
else:
    print("Not Amstrong")