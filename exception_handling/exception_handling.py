#exception - upnormal errors occurs during execution of programs
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
try:  #suspected code
  div=a/b
  print(div)
except:  #code for handling exception
    print("Not give 0 as second number")
    #or we can give
    #b=b+1
    div=a/b
    print(div)

