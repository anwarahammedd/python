class Mark:
    def getdata(self):
        self.m=int(input("Enter the mark:"))
    def printmark(self):
        print("Mark:",self.m)
class Gracemark:
    def getmark(self):
        self.gm=int(input("Enter the grace mark:"))
    def printgmark(self):
        print("Gracemark:",self.gm)
class Grade(Mark,Gracemark):
    def calcgrade(self):
        if self.m>500 or self.gm>100:
            print("Wrong")
        Total=self.m+self.gm
        p=Total/500*100
        if(p>80):
            print("Grade A")
        elif(p>70):
            print("Grade B")
        elif(p>60):
            print("Grade C")
        elif(p>50):
            print("Grade D")
        else:
            print("Just Pass")
ST1=Grade()
ST1.getdata()
ST1.printmark()
ST1.getmark()
ST1.printgmark()
ST1.calcgrade()
