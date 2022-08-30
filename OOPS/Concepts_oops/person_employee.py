class Person:
    def insert(self):
        self.voteid=int(input("Enter the Voter ID:"))
        self.name=input("Enter the Name:")
    def dis(self):
        print("VID:",self.voteid)
        print("NAME:",self.name)
class Employee(Person):
    def getdata(self):
        self.salary=int(input("Enter the Salary:"))
    def printdata(self):
        print("SALARY:",self.salary)
E1=Person()
E1.insert()
E1.dis()
E1.getdata()
E1.printdata()