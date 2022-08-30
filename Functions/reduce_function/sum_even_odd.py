import functools

lst=input("Enter the list elements").split()
newlst=list(map(int,lst))
oddlist=list(filter(lambda x:x%2!=0,newlst))
evenlist=list(filter(lambda x:x%2==0,newlst))
print(newlst)
print(oddlist)
print(evenlist)
osum=functools.reduce(lambda x,y:x+y,oddlist)
esum=functools.reduce(lambda x,y:x+y,evenlist)
print("Even sum is",esum)
print("odd sum is",osum)
