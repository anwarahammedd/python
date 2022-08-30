#filter function
#syntax
#filter(fun,sequence)

#filter even numbers
lst=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,lst)
print(list(even))

#filter odd numbers
numbers=[1,2,3,4,5,6,7,8,9]
result=filter(lambda x:x%2==1,numbers)
print(list(result))

#input numbers and print even
#numbers=input("Enter the elements:").split()
#print(numbers)
#lst1=map(int,numbers)
#even=filter(lambda x:x%2==0,lst1)
#print(list(even))

#Create a list from an existing list which have only multiple of 5
list1=[15,23,45,67,15,73,752,234,564,2423,345]
newlist=filter(lambda x:x%5==0,list1)
print(list(newlist))

#create a list which having the values greater than 5
numbers=[1,2,3,4,5,6,7,8,9,75,443,7623,454,234344,4234345,]
greatest=filter(lambda x:x>5,numbers)
print(tuple(greatest))