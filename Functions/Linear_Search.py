#Linear Search
def Linearsearch(lst,key):
    for i in lst:
        if(i==key):
            print("Key Found")
            break
    else:
        print("Key Not Found")
lst=[1,2,3,4,5,6,7,8]
key=10
Linearsearch(lst,key)
