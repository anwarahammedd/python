#Sum of first n natural numbers
n=int(input("Enter the limit:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum)