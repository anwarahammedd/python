#find the largest among Three numbers
def large(n1,n2,n3):
    if(n1>n2>n3):
        print("n1 is gretaer",n1)
    elif(n2>n3>n1):
        print("n2 is greater",n2)
    else:
        print("n3 is greater",n3)
large(5,2,7)