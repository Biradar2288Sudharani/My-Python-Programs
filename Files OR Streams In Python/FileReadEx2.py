# FileReadEx2.py
try:
    with open("C:\Python-9am\hyd.info") as fp:
        filedata=fp.readlines()
        print("*"*50)
        print(filedata)
        print("*"*50)
except FileNotFoundError:
    print("File Doesn't Exist!")



try:
    with open("C:\Python-9am\hyd.info") as fp:
        filedata=fp.readlines()
        print("*"*50)
        for record in filedata:
            print(record,end=" ")
        print("*"*50)
except FileNotFoundError:
    print("File Doesn't Exist!")






