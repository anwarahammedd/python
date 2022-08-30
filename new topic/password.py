#Password
#6-16
#a-z
#A-Z
#!@#$%^&*()
#valid
#not valid Password


import re
p=input("Enter Password:")
if len(p)<=6 or len(p)>=16:
    print("Invalid Password")
elif not re.search('[0-9]',p):
    print("Invalid Password")
elif not re.search('[a-z]',p):
    print("Invalid Password")
elif not re.search('[A-Z]',p):
    print("Invalid Password")
elif not re.search('[!@#$%^&*()]',p):
    print("Invalid Password")
else:

    print("Valid Password")
