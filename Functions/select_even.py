#even numbers
#x=[4,6,3,2]
def evenfun():
    lst=input("Enter the numbers:").split()
    evenlist=[]
    for i in lst:
        if(int(i)%2==0):
            evenlist.append(int(i))
    print(evenlist)
evenfun()

