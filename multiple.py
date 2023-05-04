import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
z='insert into JAYA(emp_id,emp_name,salary) values(%s,%s,%s)'
a=(110,'REDDY',1500),(101,'abhi',2500),(102,'madhu',2000)
cur.executemany(z,a)
mydb.commit()
print("data inserted successfully")