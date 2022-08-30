#Print a list if even find square if odd find cube
import functools

lst=input("Enter the elemnts in the list:").split()
newlist=(list(map(int,lst)))
odd=list(filter(lambda x:x%2!=0,newlist))
even=list(filter(lambda x:x%2==0,newlist))
print("Odd numbers in the list is",odd)
print("Even numbers in the list is",even)
ocube=functools.reduce(lambda x,y:x*y,odd)
esquare=functools.reduce(lambda x,y:x**y,even)
print("Cubes of odd are",ocube)
print("Squares of even are",esquare)