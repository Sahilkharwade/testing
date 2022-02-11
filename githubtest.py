import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "checking@123"
)
 
# Printing the connection object
print(mydb)
