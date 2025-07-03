# MarksExtractEx1.py
# WAPP which will extract the marks from given text.
import re
gd="mohan got 33 marks, suraj got 44 marks, yogesh got 55 marks, saurav got 66 marks, kerikeri got 77 marks,and abhijit got 88 marks"
markslist=re.findall(r"\d{2}",gd)
print("*"*50)
print("Marks Of Student")
print("*"*50)
for marks in markslist:
    print("\t{}".format(marks))
print("*"*50)



