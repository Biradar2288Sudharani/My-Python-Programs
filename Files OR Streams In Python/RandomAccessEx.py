# RandomAccessEx.py
# Program for demonstrating random access file :
with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python\\stud.data","r") as fp:
    print("*"*50)
    print("Initial Position of fp=",fp.tell())
    filedata=fp.read(6)
    print(filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())
    filedata=fp.read(4)
    print(filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())
    print("*"*50)
    filedata=fp.read(2)
    print("New Line=",filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())
    print("*"*50)
    filedata=fp.read(2)
    print("New Line=",filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())
    print("*"*50)
    filedata=fp.read(3)
    print("New Line=",filedata)
    print("*"*50)
    filedata=fp.read()
    print(filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())  # Here fp pointing to the last part of file
    print("*"*50)

# Reset the file pointer to desired index.
    fp.seek(6)
    print("Now Position of fp=",fp.tell())
    print("*"*50)
    print(filedata)
    print("*"*50)
    print("Now Position of fp=",fp.tell())
    print("*"*50)
    filedata=fp.read()
    print("After reaching end of file , File Data=",filedata)
    print("*"*50)










