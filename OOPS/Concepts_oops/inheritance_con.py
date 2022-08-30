#inheritance - Parent Class/Super class #Child class/derived #Parent-Person

#Single Inheritance - It has only one parent and child

#Parent-Person
#       Voter id
#       name
#       getdata()
#       printdata()
#Child-Employee
#      salary
#      voter id
#      name
#      getsalary()
#      getdata()
#      printsalary()
#      printdata()


class Person:
    def __init__(self,l,b):
        self.vid=l  #int(input("Enter the VID Number:"))
        self.name=b #input("Enter the Name:")
    def printdata(self):
        print("Voter ID:",self.vid)
        print("Name:",self.name)
class Employee(Person):
    def __init__(self,l,b,s):
        super().__init__(l,b)
        self.salary=s #int(input("Enter 1the Salary:"))
    def printdata(self):
        super().printdata()
        print("Salary:",self.salary)
emp1=Employee(123,"Anwar Ahammed",500000)
#emp1.getsalary()
emp1.printdata()
#emp1.printsalary()

#if the same function is present in the child and Parent. Here the Child function will display it is known as OVERRIDING.

