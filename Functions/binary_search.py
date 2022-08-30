def BinarySearch(lst,key):  #lst=[1,2,3,4,5,6,7], key=4
    mid=0
    low=0                 #low=0
    high=len(lst)-1       #high=6
    while(low<=high):      #0<=6
        mid=(low+high)//2     #(0+6)//2=3
        if(lst[mid]<key):     #lst[3]=4   4<4
            low=mid+1
        elif(lst[mid]>key):   #4>4
            high=mid-1
        else:
            return mid   #0,1,2,3,4....
    return -1
list1=[1,2,3,4,5,6,7]
key=7
f=BinarySearch(list1,key)
if(f==-1):
    print("Key not Found")
else:
    print("Key Found at",f+1)