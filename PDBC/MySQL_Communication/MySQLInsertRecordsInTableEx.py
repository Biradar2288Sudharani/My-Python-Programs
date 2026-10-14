# WAPP which will insert records in employee table
# Program for inserting the records in employee table
# import mysql.connector
# def insertrecords():
#     try:
#         con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
#         cur = con.cursor()
#         ir = "INSERT INTO Employee VALUES(101, 'Sudha', 90000, 22), (102, 'Shankar', 80000, 270), (103, 'Sachi', 100000, 24)"
#         cur.execute(ir)
#         con.commit()
#         print("Records inserted successfully --- Verify !!!") 
#         con.close()
#     except mysql.connector.DatabaseError as db:
#         print("Problem in MySQL : ", db)
# # Main Program
# insertrecords()

# OR using INPUT() method

import mysql.connector
def insertrecords():
    while(True):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
            cur = con.cursor()
            # Query for the inserting the record
            # Accept employee details from keyword
            print("*"*50)
            Emp_ID = int(input("Enter Employee ID"))
            Name = input("Enter Employee Name")
            Salary = int(input("Enter Employee Salary"))
            Age = int(input("Enter Employee Age"))
            print("*"*50)
            ir = "INSERT INTO Employee VALUES(%d, '%s', %d, %d)"
            cur.execute(ir%(Emp_ID, Name, Salary, Age))
            con.commit()
            print("*"*50)
            print("{} Employee record inserted in employee table", format(cur.rowcount))
            print("*"*50)
            ch = input("Do you want insert another record (Yes/No)")
            if (ch.lower() == "no"):
                print("Thanks for using program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB :", db)
# Main Program
insertrecords()   # Function Call
