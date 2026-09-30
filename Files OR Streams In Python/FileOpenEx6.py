# FileOpenEx6.py
'''
with open("kvr1.py","x") as fp:  # Here fp is an object of TextIOWrapper
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

# ANSWER----FileExistsError: [Errno 17] File exists: 'kvr1.py'
# Resolving the above problem existed error by using try and except i.e error hnadling concept.
'''


try:
    with open("kvr1.py","x") as fp:  # Here fp is an object of TextIOWrapper
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




