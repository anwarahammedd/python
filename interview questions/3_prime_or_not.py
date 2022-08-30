#Check given number is prime or not
n=int(input("Enter a number to check:"))
for i in range(2,n):
    if(n%i==0):
        print("Its not a prime a number")
        break
    else:
        print("Its a prime number")
        break

