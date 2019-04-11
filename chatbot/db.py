import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="ayesha",
  database="chatbot"
  )
  
mycursor = mydb.cursor()
 
name = input("name")
email = input("email")
contactmail = input("emergency contact email")
  
sql = "INSERT INTO bot (name, email, contactmail) VALUES (%s, %s, %s)"
val = (name, email, contactmail)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


#INSERT INTO `chatbot`.`bot` (`idbot`, `name`, `email`, `contact-email`) VALUES ('3', 'saima', 'ayubayesha07@gmail.com', 'ayubayesha07@gmail.com');
