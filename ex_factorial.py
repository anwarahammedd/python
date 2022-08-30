#factorial of a Number
n=int(input("Enter a Nubmer:"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("Factorial:",fact)