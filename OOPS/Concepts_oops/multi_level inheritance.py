#multi level inheritance
#A->B->C
#Student is a parent class
#     def getdata()  Roll No, Name
#     def printdata()
#Next class mark      mark->Child
#      def get mark()
#      def print mark()
#Grade -/

class Student():
    def getdata(self):
        self.rollno=int(input("Enter the Roll No:"))
        self.name=input("Enter the Name:")
    def printdata(self):
        print("Roll No:",self.rollno)
        print("Name:",self.name)
class Mark(Student):
    def getmark(self):
        self.mark=int(input("Enter the mark:"))
    def printmark(self):
        print("Mark:",self.mark)
class Grade(Mark):
    def calcgrade(self):
        p=self.mark/500*100
        if(p>=80):
            print("Grade A")
        elif(p>=70):
            print("Grade B")
        elif(p>=60):
            print("Grade C")
        elif(p>=50):
            print("Grade D")
        else:
            print("Failed")
S1=Grade()
S1.getdata()
S1.printdata()
S1.getmark()
S1.printmark()
S1.calcgrade()
