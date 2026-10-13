# program for displaying records along with column names of any table
import mysql.connector
def selectrecords():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="Shankar2sep@", database="9ambatch")
            cur = con.cursor()
            # Accept the table name
            Table_Name = input("Enter table name : ")
            sr = "SELECT * FROM %s", Table_Name
            cur.execute(sr)
            # code of getting column names
            print("*"*50)
            cloinfo = cur.description
            for col in colinfo:
                print(col[0], end = "\t\t")
            print() 
            print("*"*50)
            # code for getting records
            records = cur.fetchall()
            for record in records:
                for val in record:
                    print("{}". format(val), end="\t\t")
                print()
            print("*"*50)
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB : ", db)
# Main Program
selectrecords()  # Function Call


