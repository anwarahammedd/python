#map- map(fun,sequence)
#filter-filter(fun,sequence)
lst=[1,2,3,4,5,192,323,4,343,3434,12]
newlst=map(lambda x:x*x,lst)
print(list(newlst))

newlst1=filter(lambda x:x>10,lst)
print(list(newlst1))