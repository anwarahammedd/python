#Perfect number or not
def factors(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
           s=s+i
    if(s==num):
        print("Perfect Number")
    else:
        print("Not Perfect")
factors(5)
