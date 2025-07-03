# ClientDB.py
'''
Program-B:
Write a client side program in such a way that it should send the hall ticket number 
from server side program and obtains other details from server side program. 
'''
import socket
s=socket.socket()
s.connect(("localhost",8558))
print("CSP connected to SSP")
# get the hall ticket number from keyboard
htno=input("Enter your hall ticket number:")
s.send(htno.encode())
record=s.recv(1024).decode()
print("*"*50)
print("Result from Server")
print("*"*50)
print("Record")
print("*"*50)







