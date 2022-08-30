#factorial
def fun1(num):
    f=1
    for i in range(1,num+1): #1,2,3,4
        f=f*i  #1*1
    print("Factorial is ",f)
fun1(4)