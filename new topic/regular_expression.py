#Regular Expressions
#re.search
#import re
#str="Python Programming is fun"
#result=re.search("Python",str)          #re.search('pattern',string)
#if result:
#    print("Pattern Exist")
#else:
#    print("Pattern doesnt exist")

#re.match
#import re
#str="My Name is Anwar Ahammed"
#result=re.match("is",str)    #First Word only reads
#if result:
#    print("Pattern Matches")
#else:
#    print("Pattern doesn't matches")


#re.findall   \d     \D
import re
zipcode='122343-1212 agtb 23'
new=re.findall('\d',zipcode)
print(new)
new1=re.sub('\D','',zipcode)
print(new1)



