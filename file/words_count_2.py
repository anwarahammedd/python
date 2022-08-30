f1=open('file5','r')
lst=f1.readline()
words=lst.split()
words=set(lst.split())
print(words)
c=0
for i in words:
    c=c+1
print(c)
