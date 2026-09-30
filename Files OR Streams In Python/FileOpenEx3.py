# FileOpenWriteEx3.py
with open("kvr1.py","w") as fp:  # Here fp is an object of TextIOWrapper
    print("File Opened in Write Mode Successfully! ")
    print("Type of fp=",type(fp))
    print("File Name=",fp.name)
    print("File Mode=",fp.mode)
    print("\tFile Readable=", fp.readable())
    print("\tFile Writable=", fp.writable())
    print("\tFile Closed=", fp.closed)
    print("\tFile Closed After With Open() as=",fp.closed)

''' --> ANSWER <--
File Opened in Write Mode Successfully! 
Type of fp= <class '_io.TextIOWrapper'>
File Name= kvr1.py
File Mode= w
	File Readable= False
	File Writable= True
	File Closed= False
	File Closed After With Open() as= False
'''










