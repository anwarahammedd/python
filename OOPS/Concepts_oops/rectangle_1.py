class Rectangle:
    def read(self,l,b):
        self.length=l    #variable_name    -   Public data number
        self.__breadth=b   #__variable_name  -  Private data number
    def display(self):
        print("Length:",self.length)
        print("Breadth:",self.__breadth)
R1=Rectangle()
R1.read(5,2)
R1.display()
print(R1.length)
print(R1.__breadth)
