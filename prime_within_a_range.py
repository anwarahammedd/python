#50-100 Any Prime Numbers
for i in range(50,100):
    for j in range(2,i-1):
        if(i%j==0):
             break
    else:
        print(i,end=" ")