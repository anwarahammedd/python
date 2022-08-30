def add(num1,num2):
    s=num1+num2
    print("Sum is",s)
def sub(num1,num2):
    d=num1-num2
    print("Difference is",d)
def mul(num1,num2):
    d=num1*num2
    print("Product is",d)
def div(num1,num2):
    p=num1/num2
    print("Quoteint is",p)
while(True):
    print(1,"Addition")
    print(2,"Subtraction")
    print(3,"Multiplication")
    print(4,"Division")
    c=int(input("Enter your choice:"))
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if(c==1):
        add(a,b)
    elif(c==2):
        sub(a,b)
    elif(c==3):
        mul(a,b)
    elif(c==4):
        div(a,b)
    else:
        print("Wrong Choice")
        break