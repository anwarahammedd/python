#constructor - Used to initialize data members  __init__
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def dis(self):
        print("Length:",self.length)
        print("Breadth:",self.breadth)
R1=Rectangle(10,5)
R2=Rectangle(20,50)
R1.dis()
R2.dis()