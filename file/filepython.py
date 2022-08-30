#file jpef,doc,png
#fileobject=open(file_name,mode)
#mode
#r - read
#r+ - read and write
#w - write
#w+ - write and read
#a - append
#read - read content from file
f1=open('file1','r')
#print("First location:",f1.tell())
print(f1.read(3))
#print("Second Location:",f1.tell())
print(f1.read(3))
#print("Third Location:",f1.seek(0))
print(f1.read(3))
print(f1.read(10))
print(f1.read(1))
f1.close()
