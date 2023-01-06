import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Sparky@6@21998")
mycursor = mydb.cursor()
mycursor.execute("select * from vijay.sftpaudit;")
result = mycursor.fetchall()
for i in result:
  print (i)
