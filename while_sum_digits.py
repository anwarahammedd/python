#Find the sum of digits of a number
#123=6

#123%10  d=3   sum=sum+d
#123//10=12

#12%10=2  d=2
#12//10=1

#1%10=1  d=1
#1//10=0
n=int(input("Enter Number::"))
sum=0
while(n>0):
    d=n%10
    n = n // 10
    sum=sum+d
print(sum)
