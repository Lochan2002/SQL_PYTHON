import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002',database='LOCHAN')
cur=mydb.cursor()
f='select * from JAYA'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)