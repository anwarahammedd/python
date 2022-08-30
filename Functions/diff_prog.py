#Input a string : Sun rises in the east
#in
#east

n=input("Enter the string:").split()
print(n)
for i in n:
    if(len(i)%2==0):
        print(i)
