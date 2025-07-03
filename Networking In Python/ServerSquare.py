# ServerSquare.py
'''
Program-B:
Write a python server side program which will accept a number from client side program,
performs it's execution.  
'''
import socket
ss=socket.socket()
ss.connect("localhost",9999)
print("Server side program is ready to accept client side program request!!!")
while(True):
    try:
        cs,ca=ss.accept()
        cdata=cs.recv(1024).decode()
        print("Value of client at server=",cdata)
        v=float(cdata)
        res=v**2
        cs.send(str(res).encode())
    except ValueError:
        cs.send("Don't enter str,alnums and symbols".encode())









