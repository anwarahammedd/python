#variable length arguments )args
def var_length(*arg):
    print(type(arg))
    for i in arg:
        print(i)
var_length(10,20)
var_length(1,2,3,4,6)