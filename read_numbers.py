# Read one numbers
# >10  big
#  10  expected number
#  <10 Small

n=int(input("Enter the Number:"))
if(n>10):
    print("big")
elif(n==10):
    print("Expected Number")
else:
    print("Small")