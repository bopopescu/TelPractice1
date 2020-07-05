import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="telusko")
mycursor=mydb.cursor()
#mycursor.execute("show databases")
mycursor.execute('select * from Students')
result=mycursor.fetchall()
print(result)
for i in mycursor:
    print(i)

