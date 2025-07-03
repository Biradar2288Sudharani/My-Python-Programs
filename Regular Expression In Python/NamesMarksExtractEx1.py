# NamesMarksExtractEx1.py
# WAPP for obtaining names and marks of students from given text.
import re
gd="Mohan got 33 marks, Suraj got 44 marks, Yogesh got 55 marks, Saurav got 66 marks, Kerikeri got 77 marks,and Abhijit got 88 marks"
nameslist=re.findall("[A-Z][a-z]+",gd)
markslist=re.findall(r"\d{2}",gd)
print("*"*50)
print("\t Names \t\t Marks")
print("*"*50)
for names,marks in zip(nameslist,markslist):
    print("\t{}\t\t{}".format(names,marks))
print("*"*50)


