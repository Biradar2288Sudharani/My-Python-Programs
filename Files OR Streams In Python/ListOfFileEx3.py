# ListOfFileEx3.py
# Program for listing the file or display the file names in folder.
import os
try:
    foldername=input("Enter Folder Name:")
    FileNames=os.listdir("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Files OR Streams In Python") # Here FileNames is an object of listtype.
    print("*"*50)
    print("List Of Files")
    print("*"*50)
    nopy=0
    for filename in FileNames:
        if(filename[-1]=="py"):
            nopy=nopy+1
            print("\t\t{}".format(filename))
    print("*"*50)
    print("Number Of File={}".format(len(FileNames)))
    print("Number Of Python File={}".format(nopy))
except FileNotFoundError:
    print("Folder Doesn't Exist!!!")