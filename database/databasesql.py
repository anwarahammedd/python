import pymysql
db=pymysql.connect(host='localhost',user='root',password='4121',db='db3')
#prepare cursor object using cursor() method
cur1=db.cursor()
sql='insert into Product (Id,name) values (1,"Computer"),(2,"Laptop")'
cur1.execute(sql)
db.commit()