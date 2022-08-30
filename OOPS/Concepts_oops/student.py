class Student:
    def read(self):
        self.rollno=int(input("Enter the roll no.:"))
        self.name=input("Enter the name:")
    def display(self):
        print("Roll No",self.rollno)
        print("Name",self.name)
#objectname=classname
s1=Student()
s1.read()
s1.display()
s2=Student()
s2.read()
s2.display()
s3=Student()
s3.read()
s3.display()