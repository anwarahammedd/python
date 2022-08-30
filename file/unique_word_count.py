#number of words
def wordcount(lst):
    dict={}
    for i in lst:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    for a,b in dict.items():
        print(a,":",b)
f1=open('file5','r')
r=f1.read()
words=r.split()
wordcount(words)
