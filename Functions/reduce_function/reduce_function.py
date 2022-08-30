#reduce function
#[1,2,3,4,5]=15
#To perform an operation which makes single value
import functools
lst=[1,2,3,4,5,6]
result=functools.reduce(lambda x,y:x+y,lst)  #reduce(fun,sequence)
print(result)
