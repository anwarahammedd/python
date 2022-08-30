#fibonacci Series
n=int(input("Enter the Limit:"))
f=0
s=1
t=0
print(f,s,end=" ")
for i in range(2,n):
    t=f+s
    f=s
    s=t
    print(t,end=" ")
