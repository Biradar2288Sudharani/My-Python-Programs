# FileCopyEx1.py
# WAPP which will copy the content of one file into another file.
'''
To copy the one file into another file two files are required.
    * File1--> SOurce File
    * File2--> Destination File
    * Open source file in read mode 
    * Open destination file in write mode
    * Read the data from source file and write to destination file
    * If source file does not exist then display "Source file doesn't exist"
'''

srcfile=input("Enter Source File: ")
try:
    with open (srcfile,"r") as fp:
        destfile=input("Enter Destination File: ")
        with open(destfile,"a") as wp:
            srcfiledata=fp.read()
            wp.write(srcfiledata)
            print("Source File Content Copied Into Destination File---Verify!!!")
except FileNotFoundError:
    print("Source File Doesn't Exist.")       



















