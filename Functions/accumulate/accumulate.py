#1
import itertools
lst=[1,2,3,4,5]
res=itertools.accumulate(lst) #accumulate(seq,fun)
print(list(res))

#2
import itertools
lst=[1,2,3,4]
mid=itertools.accumulate(lst,lambda x,y:x+y)
print(list(mid))
