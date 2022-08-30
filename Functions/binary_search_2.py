def BinarySearch(lst,key):  #lst=[88,55,66,77,44,3,6,8], key=55   sort(lst)=[3,6,8,44,55,66,77,88]
    low=0                   #low=0
    mid=0
    high=len(lst)-1         #high=7
    while(high>=low):       #7>=0
        mid=(low+high)//2   #(0+7)//2=3
        if(lst[mid]<key):   #44<55
            low=mid+1
        if(lst[mid]>key):
            high=mid-1
        else:
            return mid
    return -1
list1=input("Enter the List:").split()
list.sort(list1)
print(list1)
key=input("Enter a value to search:")
f=BinarySearch(list1,key)
if(f==-1):
    print("Not Present")
else:
    print("Present in",f+1)