# ServerDB.py
'''
Program-A:
Write a server side program in such a way that it should recieve the hall ticket 
number from client side program and gives other details to client side program.
'''
import socket
import oracledb as orc
ss=socket.socket()
ss.bind(("localhost",8558))
ss.listen(2)
print("SSP is ready to accept CSP request")
while(True):
    try:
        cs,ca=ss.accept()
        htno=int(cs.recv(1024).decode())
        # Write PDBC Code
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        cur.execute("select * from studentresult where hall ticket number=%d"%htno)
        Record=cur.fetchone()
        if(Record!=None):
            line1="Student Hall Ticket Number:{}".format(Record[0])
            line2="Student Name:{}".format(Record[1])
            line3="Student Total Marks:{}".format(Record[2])
            line4="Student Rank:{}".format(Record[3])
            result=line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"
            cs.send(result.encode())
        else:
            cs.send("Your hall ticket number is invalid".encode())

    except ValueError:
        cs.send("Don't enter strs, symbols and alnums".encode())
    except orc.DatabaseError as db:
        cs.send(("Problem in oracleDB:"+db).encode())











