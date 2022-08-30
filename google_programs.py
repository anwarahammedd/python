#Python Program to Display Powers of 2 Using Anonymous Function
number=[1,2,3,4,5,6,7,8,9,10]
answer=[filter(lambda x:2**x,number)]
print(list(answer))

