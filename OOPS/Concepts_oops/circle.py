#circle
#circumference
#area
#radius
class circle:
    def getdata(self):
        self.radius=int(input("Enter the radius:"))
    def display(self):
        print("Radius of the circle is",self.radius)
    def area(self):
        a=3.14*self.radius*self.radius
        print("Area of the circle is",a)
C1=circle()
C1.getdata()
C1.display()
C1.area()