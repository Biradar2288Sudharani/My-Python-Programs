# FileOpenReadEx4.
try:
    fp=open("kvr1.py","r")  # Here fp is an object of TextIOWrapper
except FileNotFoundError:
    print("File Doesn't Exist!")
else:
    print("*"*50)
    print("File Opened in Write Mode Successfully! ")
    print("Type of fp=",type(fp))
    print("*"*50)
    print("Properties of File...")
    print("*"*50)
    print("File Name=",fp.name)
    print("File Mode=",fp.mode)
    print("\tFile Readable=", fp.readable())
    print("\tFile Writable=", fp.writable())
    print("\tFile Closed in else Block=", fp.closed)
    print("\tFile Closed After With Open() as=",fp.closed)
    print("*"*50)
finally:
    fp.close()  # Manual Closing
    print("\t Closed in Finally Block =",fp.closed)


''' --> ANSWER <--
**************************************************
File Opened in Write Mode Successfully! 
Type of fp= <class '_io.TextIOWrapper'>
**************************************************
Properties of File...
**************************************************
File Name= kvr1.py
File Mode= r
	File Readable= True
	File Writable= False
	File Closed in else Block= False
	File Closed After With Open() as= False
**************************************************
	\s Closed in Finally Block = True
'''










