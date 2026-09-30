# FileReadEx1.py
with open("stud.data") as fp:
    filedata=fp.read()
    print(type(filedata))


try:
    with open("stud1.data") as fp:
        filedata=fp.read()
        print(type(filedata))
except FileNotFoundError:
    print("File Does Not Exist!!!!")


try:
    with open("stud1.data") as fp:
        #OR
        with open("stud1.data") as fp:
            filedata=fp.read()
            print("*"*50)
            print("Filedata")
            print("*"*50)
except FileNotFoundError:
    print("File Doesn't Exist!")








