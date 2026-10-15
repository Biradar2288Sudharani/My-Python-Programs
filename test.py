
# WAPP which will create a table Employee with suitable columns in 9ambatch database of mysql
# Program for creating a table employee in 9ambatch of mysql
import mysql.connector
def tablecreate():
    try:
        con = mysql.connector.connect(host = "Localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
        cur = con.cursor()
        # Design the query and execute
        tc = "CREATE TABLE Employees(Emp_ID INT PRIMARY KEY, Name VARCHAR(100), Salary INT)"
        cur.execute(tc)
        print("Table created successfully !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL ", db)
# Main Program
tablecreate()

# WAPP which will alter the column size
# Program for alter the column sizes in Employee table and 9ambatch database

import mysql.connector
def altercolumnsize():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch" )
        cur = con.cursor()
        ats = "ALTER TABLE Employee MODIFY Name VARCHAR(110)"
        cur.execute(ats)
        print("Alter column size is done !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL :", db)
# Main Program
altercolumnsize()

# WAPP which will alter the column size
# Program for alter the column sizes in Employee table and 9ambatch database

import mysql.connector
def altercolumnsize():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch" )
        cur = con.cursor()
        ats = "ALTER TABLE Employee MODIFY Name VARCHAR(110)"
        cur.execute(ats)
        print("Alter column size is done !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL :", db)
# Main Program
altercolumnsize()

# WAPP which will alter the column size
# Program for alter the column sizes in Employee table and 9ambatch database

import mysql.connector
def altercolumnsize():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch" )
        cur = con.cursor()
        ats = "ALTER TABLE Employee MODIFY Name VARCHAR(110)"
        cur.execute(ats)
        print("Alter column size is done !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL :", db)
# Main Program
altercolumnsize()

# WAPP which will alter the column size
# Program for alter the column sizes in Employee table and 9ambatch database

import mysql.connector
def altercolumnsize():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch" )
        cur = con.cursor()
        ats = "ALTER TABLE Employee MODIFY Name VARCHAR(110)"
        cur.execute(ats)
        print("Alter column size is done !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL :", db)
# Main Program
altercolumnsize()

# WAPP which will alter the column size
# Program for alter the column sizes in Employee table and 9ambatch database

import mysql.connector
def altercolumnsize():
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch" )
        cur = con.cursor()
        ats = "ALTER TABLE Employee MODIFY Name VARCHAR(110)"
        cur.execute(ats)
        print("Alter column size is done !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL :", db)
# Main Program
altercolumnsize()