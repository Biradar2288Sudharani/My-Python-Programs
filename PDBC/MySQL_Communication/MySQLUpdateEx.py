# WAPP which will update salary and age of employee table of masql database
import mysql.connector
def recordupdate():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="Shankar2sep@", database="9ambatch")
            cur = con.cursor()
            # design the query
            Emp_ID = int(input("Enter employee id for updating other details : "))
            Salary = int(input("Enter employee new salary : "))
            Age = int(input("ENter employee new age : "))
            rd = "UPDATE Employee SET Salary = %d, Age = %d WHERE Emp_ID = %d"
            cur.execute(rd%(Salary, Age, Emp_ID))
            con.commit()
            if(cur.rowcount > 0):
                print("{} Employee record updated". format(cur.rowcount))
            else:
                print("Employee record does not exist")
            print("*"*50)
            ch = input("Do you want to update another record(Yes/No)")
            if(ch.lower()=="no"):
                print("Thanks for using this program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB : ", db)
# Main Program
recordupdate()  # Function Call


            
            
