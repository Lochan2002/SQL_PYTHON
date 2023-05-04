import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
s='delete from JAYA where emp_id=110'
cur.execute(s)
mydb.commit()