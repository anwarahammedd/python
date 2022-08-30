#simple calculator
#Enter two numbers
#1 Addition
#2 Subtract
#3 Multiplication
#4 Division

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(1,"Addition")
print(2,"Subtraction")
print(3,"Multiplication")
print(4,"Division")
ch=int(input("Enter your choice:"))
if(ch==1):
    result=num1+num2
    print(result)
elif(ch==2):
    result=num1-num2
    print(result)
elif(ch==3):
    result=num1*num2
    print(result)
elif(ch==4):
    result=num1/num2
    print(result)
else:
    print("wrong choice")


