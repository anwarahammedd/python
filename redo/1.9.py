#Read marks of three subjects(100)
#(total mark/300)*100
#>=80 Grade A
#60-79 Grade B
#50-59 Grade C
#40-49 Grade D
#Below 40-Failed

s1=int(input("Enter the mark 1:"))
s2=int(input("Enter the mark 2:"))
s3=int(input("Enter the mark 3:"))
TM=s1+s2+s3
perc=(TM/300)*100
if(perc>=80 && perc<101):
    print("Grade A")
elif(perc>=60 && perc<80):
    print("Grade B")
elif(perc>=50 && perc<60):
    print("Grade C")
elif(perc>=40 && perc<50):
    print("Grade D")
elif(perc<40):
    print("Failed")
else:
    print("Wrong Input")