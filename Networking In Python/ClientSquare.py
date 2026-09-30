# ClientSquare.py
'''
PROGRAM-A:
Write a python client side program in such a way that it should accept a number from 
keyboard, sent. 
'''
import socket
s=socket.socket()
s.connect("localhost",9999)
print("Client Side Program Obtains Connections From Server Side Program!!!")
print("*"*50)
val=input("Enter a Number for getting it's Square:")
s.send(val.encode())
result=s.recv(1024).decode()
print("Square ({})={}".format(val,result))
print("*"*50)












