import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
z='insert into JAYA(emp_id,emp_name,salary) values(%s,%s,%s)'
a=(100,'REDDEY',1000)
cur.execute(z,a)
mydb.commit()
print("data inserted successfully")