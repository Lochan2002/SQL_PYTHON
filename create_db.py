import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Lochan@2002')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database LOCHAN')