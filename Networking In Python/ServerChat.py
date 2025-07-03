# ServerChat.py
# Write a Network based OR Console based chatting application.
'''
Program-A:
Write a server side python program in such a way that servser side program must
recieve the message from client side program and gives repaly or answer to the client
side program.
'''
import socket
ss=socket.socket()
ss.bind(("127.0.0.1",8888))
ss.listen(2)
print("SSP is ready to accept any CSP request!!!")
while(True):
    cs,ca=ss.accept()
    cdata=cs.recv(1024).decode()
    print("Student--->{}".format(cdata))
    # Server side program reads replay message from keyboard
    sdata=input("KVR--->:")
    cs.send(sdata.encode())










