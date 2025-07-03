# NamesMarksExtractEx2.py
# WAPP for obtaining names and marks of students from given text.
# Doubt in this program

import re
try:
    with open("C:\\Users\\lenovo\\Desktop\\Library\\ONLY KVR PYTHON\\KVR Lecture Program\\Regular Expression In Python\\student.txt","r") as fp:
        filedata=fp.read
        nameslist=re.findall("[A-Z][a-z]+",filedata)
        markslist=re.findall(r"\d{2}",filedata)
        print("*"*50)
        print("\t Names \t\t Marks")
        print("*"*50)
        for names,marks in zip(nameslist,markslist):
            print("\t{}\t\t{}".format(names,marks))
        print("*"*50)
except FileNotFoundError:
    print("File Doesn't Exist")


