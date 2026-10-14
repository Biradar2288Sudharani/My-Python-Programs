# WAPP which will delete the records by accept based on employee id
# import mysql.connector
# def deleterecord():
#     try:
#         con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
#         cur = con.cursor()
#         dr = "DELETE FROM Employee WHERE Emp_ID = 104"
#         cur.execute(dr)
#         con.commit()
#         print("Employee table record deleted successfully !!!")
#         con.close()
#     except mysql.connector.DatabaseError as db:
#         print("Problem in MySQL DB: ", db)
# # Main Program
# deleterecord()   # Function Call

# OR Using INPUT Method
import mysql.connector
def deleterecord():
    while(True):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Shankar2sep@", database = "9ambatch")
            cur = con.cursor()
            # Prepare the query and execute
            print("*"*50)
            Emp_ID = int(input("Enter Employee ID for deleting record : "))
            cur.execute("DELETE FROM Employee WHERE Emp_ID = %s" , (Emp_ID, ))
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee record deleted". format(cur.rowcount))
            else:
                print("Employee record does not exists")
            print("*"*50)
            ch = input("Do you want to delete another record (Yes/No)")
            if (ch.lower()=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB : ", db)
# Main Program
deleterecord()  # Function Call















