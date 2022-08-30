#lambda ar1,ar2,.....:expression
lar=lambda x,y:x if x>y else y
a=int(input("Enter the First Number:"))
b=int(input("Enter the second Number"))
print("Largest is",lar(a,b))