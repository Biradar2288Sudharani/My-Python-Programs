# FileReadEx3.py
# Program for displaying the content of any file.
try:
    filename=input("Enter any file name:")
    with open(filename,"r") as fp:
        filedata=fp.read()
        print("*"*50)
        print("Content of '{}' file:".format(filename))
        print("*"*50)
        print("{}".format(filedata))
        print("*"*50)
except FileNotFoundError:
    print("File Does Not Exist!!")
    











