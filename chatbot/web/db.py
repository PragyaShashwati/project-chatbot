#!C:\Program Files (x86)\Python37-32\python.exe

import mysql.connector
import cgi


data = cgi.FieldStorage()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="ayesha",
  database="chatbot"
  )
  
mycursor = mydb.cursor()
 
name = data.getvalue("name")
email = data.getvalue("email")
contactmail = data.getvalue("contactmail")
  
sql = "INSERT INTO bot (name, email, contactmail) VALUES (%s, %s, %s)"
val = (name, email, contactmail)
mycursor.execute(sql, val)
mydb.commit()
print('location: http://localhost/chatbot/web/api.html\r\n\r\n')





