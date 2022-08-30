#variable length arguments
def fun1(*args):
    print(type(args))
    for i in args:
        print(i)
fun1(10,20,30,"anwar",23,4,2)
print("call2")
fun1(5,6,7,4)
fun1(4,5,3,1,3,4)
