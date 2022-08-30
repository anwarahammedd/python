import re
f1=open('file6','r')
text=f1.readlines()
for line in text:
    result=re.search(r'\bs\w*e\b',line)
    if(result):
        print(line)



