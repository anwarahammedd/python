#Fahrenheit to Celsius
#Celcius to Fahrenheit
print(1,"Celsius to Fahrenheit")
print(2,"Fahreheit to Celsius")
ch=int(input("Enter your Choice::"))
if(ch==1):
    c=float(input("Enter the temprature in celsius:"))
    f=(c*9/5)+32
    print("Temptaure in Fahreheit is",f)
elif(ch==2):
    f=float(input("Enter the Celsius in Temprature:"))
    c=(f-32)*5/9
    print("Temprature in Fahrenheit is",c)
else:
    print("Wrong Choice")

