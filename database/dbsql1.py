import pymysql
db=pymysql.connect(host='localhost',user='root',password='4121',db='db3')
cur1=db.cursor()
#sql='insert into Students(id,name) values(1,"Anwar"),(2,"Ahammed"),(3,"Anu"),(4,"Ameen"),(5,"Anas")'
sql="select * from Students"
cur1.execute(sql)
row=cur1.fetchone() #fetch all the records from the table
print("ID  NAME")
#for i in rows:
#    print(i[0],':',i[1])
if row:
    print(row[0],row[1])
db.commit()


#fetchall()
#fetchone()

