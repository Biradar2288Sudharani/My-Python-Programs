# ClientChat.py
'''
Program-B:
Write a client side program in such a way that client side program must read the 
message from keyboard and send to server program and gets the replay OR answer
from server side program.
'''

import socket
while(True):
    s=socket.socket()
    s.connect(("127.0.0.1",8888))
    # CSP must read the data from keyboard for sending to server side program
    cdata=input("Student--->:")
    if(cdata.lower()=="bye"):
        s.send(cdata.encode())
        break
    else:
        s.send(cdata.encode())
        sd=s.recv(1024).decode()
        print("KVR--->:{}".format(sd))

















