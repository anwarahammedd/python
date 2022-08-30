#variable length arguments **kargs -keyword argument
def fun(**karg):  #dictionary
    print(type(karg))
    for k,v in karg.items():
         print(k,":",v)
fun(Name='Anu',cls='BCA')
