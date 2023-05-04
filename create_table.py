import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
t='create table JAYA(emp_id integer(4),emp_name varchar(30),salary integer(10))'
cur.execute(t)