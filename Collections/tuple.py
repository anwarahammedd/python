#tuple - #immutable - elements cannot be changed
#tuple=(1,4,5,6.8,'anu')

##########################
#tuple1=(1,3,4,4.5,'anu')
#tuple1[1]=25
#print(tuple1)
#############################

#count
#tuple1=(1,3,4,6.6,'anu',1,1)
#print(tuple1.count(1))

#index
#tuple1=(1,4,5,6,4.4,'anu',4,5)
#print(tuple1.index())

#max
#tuple1=(1,3,4,5,6.6)
#print(max(tuple1))

#min
#tuple1=(1,4,5,6,7.5)
#print(min(tuple1))

#find the sum of elements in the tuple
#tuple1=(1,5,1,2,4,6)
#sum=0
#for i in tuple1:
#    sum=sum+i
#print(sum)
#or
#tuple1=(1,5,1,2,4,6)
#print(sum(tuple1))

#read a tuple and search a particular element.
item=input("Enter the Elements").split()
print(item)
tuple1=tuple(item)
print(tuple1)
n=int(input("Item to be searched:"))
for i in tuple1:
    if i==n:
        print("Item Found")
        break
else:
    print("item not found")

