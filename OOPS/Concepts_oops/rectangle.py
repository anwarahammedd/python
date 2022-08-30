#rectangle
#length
#breadth
#getdata()
#display()

class Rectangle():
    def getdata(self,l,b):
        self.length=l
        self.breadth=b
    def displaydata(self):
        print("Length:",self.length)
        print("Breadth:",self.breadth)
    def area(self):
        a=self.length*self.breadth
        print("Area is",a)
R1=Rectangle()
R1.getdata(10,5)
R1.displaydata()
R1.area()

