#Simple Number
number=[i for i in range(1,10)]
print(number)

#Square of Simple numbers
square=[i*i for i in range(1,8)]
print(square)

#Even Numbers
even=[i for i in range(1,10) if i%2==0]
print(even)

#Odd numbers
odd=[i for i in range(1,10) if i%2==1]
print(odd)

#flower list
flowers=['lilly','lotus','sunflower','jasmine','rose','daffodils']
newflower=[i.upper() for i in flowers if 'o' in i ]
print(newflower)
#newflowers=['LILLY','LOTUS','ROSE','HIBISCUS']

#Print any one flower out.
flower=['lilly','daffodils','lotus','jasmine']
newflower=[i for i in flower if i!='lilly']
print(newflower)

#