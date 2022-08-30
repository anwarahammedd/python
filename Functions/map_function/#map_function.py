#map function - To change the reflection of all values
#map(fun,sequence)


def multi(n):
    return n*n
numbers=[1,2,3,4]
result=map(multi,numbers)
print (tuple(result))

#using lambda function
num=(1,2,3,4,5)
result=map(lambda n:n*n,num)
print(list(result))

