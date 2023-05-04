import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
x='update JAYA set salary=salary+100 where emp_id=101'
cur.execute(x)
mydb.commit()