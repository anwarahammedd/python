#Calculator
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(1,"Addition")
print(2,"Subtraction")
print(3,"Multiplication")
print(4,"Division")
ch=int(input("Enter your choice"))
if(ch==1):
    sum=num1+num2
    print("Sum is",sum)
elif(ch==2):
    diff=num1-num2
    print("Difference is",diff)
elif(ch==3):
    pro=num1*num2
    print("Product is",pro)
elif(ch==4):
    div=num1/num2
    print("Quoteint is",div)
else:
    print("Wrong Choice")
