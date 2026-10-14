# WAPP which will remove the table
# program for removing Employees table in 9ambatch database

import mysql.connector
def removetable():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
        cur = con.cursor()
        rt  = "DROP TABLE Employees"
        cur.execute(rt)
        print("Employees table removed successfully --- Verify!!!")
    except mysql.connector.DatabaseError as db:
        print("Problme in MySQL : ", db)
# Main Program
removetable()  # Function Call