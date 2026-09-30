# NamesMailsExtractEx1.py
# Program for obtaining names and marks of student from given file ---> mails info
# Doubt in this program
import re
try:
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Regular Expression In Python\\mails_info.txt","r") as fp:
        filedata=fp.read()
        nameslist=re.findall("[A-Z][a-z]+",filedata)
        mailslist=re.findall(r"\s+@+\s",filedata)
        print("*"*50)
        print("\t Names \t\t Mail ID")
        print("*"*50)
        for names,mails in zip(nameslist,mailslist):
            print("\t{}\t\t{}".format(names,mails))
        print("*"*50)
except FileNotFoundError:
    print("File Doesn't Exist.")









