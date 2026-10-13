# WAPP which will create a database name.
# Program for creating a database on the name of "9ambatch".
import mysql.connector
con = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "Shankar2sep@")
print("Python program got connection from mysql database!")
cur = con.cursor()
# Design the query and execute
dc = "Create Database 9ambatch"
cur.execute(dc)
print("Database created in MySQL --- Verify !!!")