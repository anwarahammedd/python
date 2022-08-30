print(1,"Display Account Detials")
print(2,"Deposit")
print(3,"Withdraw")
print(4,"Balance Enquiry")
print(5,"Exit")
n=int(input("Enter the input:"))
while(n==1):
      print("Account Details")
      break
class Bank:
    def getdata(self):
        self.name=input("Enter the Name of Depositer:")
        self.acnumber=int(input("Enter the Account Number:"))
        self.typeac=input("Type of Account:")
        self.balance=0
while(n==2):
    print("Amount to be deposited")
    break
    def deposit(self):
        d=int(input("Enter the amount to be deposited"))
        self.balance=self.balance+d
    def withdraw(self):
        w=int(input("Enter the amount to be withrawed"))
        if(self.balance>=w):
            self.balance=self.balance-w
            print("New Balance",self.balance)
        else:
            print("Insufficeint Funds")
    def display(self):
        print("Name:",self.name)
        print("Account Number",self.acnumber)
        print("Type of Account",self.typeac)
        print("Balance",self.balance)
obj1=Bank()
obj1.getdata()
obj1.deposit()
obj1.withdraw()
obj1.display()

#1-display account details
#2-Deposit
#3-Withdraw
#4-Balalnce Enquiry
#5-Exit
#Enter the option