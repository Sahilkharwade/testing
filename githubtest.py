import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "checking@123"
)
 
# Printing the connection object
print(mydb)


import requests
url = 'https://updates.opendns.com/nic/update?hostname='
username = 'username'
password = 'password'
print(requests.get(url, auth=(username, password)).content)
