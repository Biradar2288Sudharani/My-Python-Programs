# WAPP which will drop or remove any database
# Program for droping or removing database from MySQL
import mysql.connector
def dropdatabase():
    try:
        con = mysql.connector.connect(host = "Localhost", user = "root", password = "Shankar2sep@")
        cur = con.cursor()
        # Design the query and execute
        cur.execute("Drop database sudharani")
        print("Database removed from mysql --- Verify !!!")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL : ", db)
# Main Program
dropdatabase()    # Function call