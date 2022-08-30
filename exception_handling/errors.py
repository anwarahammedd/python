try:
 a=int(input("Enter the first number:"))
 b=int(input("Enter the second number:"))
 c=a/b
 print(d)
except ValueError:
    print("You must enter a number")
except ZeroDivisionError:
    print("Enter the second number other than zero")   #also we can give like this  #except (ValueError,ZeroDivisionError):
except:
    print("All other errors handle error")
else:
    print("Execute if there is no errors")
finally:
    print("Always Execute")


#ZeroDivisionError -
#NameError - Variable not defined
#ValueError - if we give string instead of integer
