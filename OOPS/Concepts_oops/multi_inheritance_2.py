class Student():
    def __init__(self):
        self.name=input("Enter the name of the Student:")
        self.rollno=int(input("Enter the Roll No:"))
    def printdata(self):
        print("Name:",self.name)
        print("Roll No:",self.name)
class Mark(Student):
    def __init__(self):
        self.mark=int(input("Enter the mark out of 500:"))
    def printmark(self):

