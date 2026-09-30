# FileOpenEx5.py
# Example 1
with open("kvr1.py","w+") as fp:  # Here fp is an object of TextIOWrapper
    print("*"*50)
    print("File Opened in Write Mode Successfully! ")
    print("Type of fp=", type(fp))
    print("*" * 50)
    print("Properties of File...")
    print("*" * 50)
    print("File Name=", fp.name)
    print("File Mode=", fp.mode)
    print("\tFile Readable=", fp.readable())
    print("\tFile Writable=", fp.writable())
    print("\tFile Closed in else Block=", fp.closed)
    print("\tFile Closed After With Open() as=", fp.closed)
    print("*" * 50)

fp.close()  # Manual Closing
print("\t Closed in Finally Block =", fp.closed)
print("#" * 50)



# Example 2
with open("kvr1.py","r+") as fp:  # Here fp is an object of TextIOWrapper
    print("*"*50)
    print("File Opened in Write Mode Successfully! ")
    print("Type of fp=", type(fp))
    print("*" * 50)
    print("Properties of File...")
    print("*" * 50)
    print("File Name=", fp.name)
    print("File Mode=", fp.mode)
    print("\tFile Readable=", fp.readable())
    print("\tFile Writable=", fp.writable())
    print("\tFile Closed in else Block=", fp.closed)
    print("\tFile Closed After With Open() as=", fp.closed)
    print("*" * 50)

fp.close()  # Manual Closing
print("\t Closed in Finally Block =", fp.closed)
print("#" * 50)



# Example 3
with open("kvr1.py","a+") as fp:  # Here fp is an object of TextIOWrapper
    print("*"*50)
    print("File Opened in Write Mode Successfully! ")
    print("Type of fp=", type(fp))
    print("*" * 50)
    print("Properties of File...")
    print("*" * 50)
    print("File Name=", fp.name)
    print("File Mode=", fp.mode)
    print("\tFile Readable=", fp.readable())
    print("\tFile Writable=", fp.writable())
    print("\tFile Closed in else Block=", fp.closed)
    print("\tFile Closed After With Open() as=", fp.closed)
    print("*" * 50)

fp.close()  # Manual Closing
print("\t Closed in Finally Block =", fp.closed)
print("#" * 50)