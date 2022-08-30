#Read marks of three subjects(100)
#(total mark/300)*100
#>=80 Grade A
#60-79 Grade B
#50-59 Grade C
#40-49 Grade D
#Below 40-Failed

s1=int(input("Enter the mark of S1:"))
s2=int(input("Enter the mark of S2:"))
s3=int(input("Enter the mark of S2:"))
if(s1<=100 and s2<=100 and s3<=100):
     total=s1+s2+s3
     percentage=(total/300)*100
     print(total,"is the total mark")
     print(percentage,"is the percentage")
     if(percentage>=80):
          print("Grade A")
     elif(percentage>=60 and percentage<79):
          print("Grade B")
     elif(percentage>=50 and percentage<59):
        print("Grade C")
     elif(percentage>=40 and percentage<49):
        print("Grade D")
     elif(percentage<40):
        print("failed")
else:
    print("wrong input")
