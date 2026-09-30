# FileOpenEx7.py
# Creating kvr2.py file
try:
    with open("kvr2.py","x") as fp:  # Here fp is an object of TextIOWrapper
        print("*"*50)
        print("File Opened in exclusively Write Mode Successfully! ")
        print("Type of fp=", type(fp))
        print("*" * 50)
        print("Properties of File...")
        print("*" * 50)
        print("File Name=", fp.name)
        print("File Mode=", fp.mode)
        print("\tFile Readable=", fp.readable())
        print("\tFile Writable=", fp.writable())
        print("\tFile CLosed=",fp.closed)
        print("*"*50)
    print("\t File Closed After With Open() As=",fp.closed)
except FileExistsError:
    print("File Already Existed!!")










