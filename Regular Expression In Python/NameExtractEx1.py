# NameExtractEx1.py
# WAPP which will extract names of the students from the given text.
import re
gd="Mohan got 33 marks, Suraj got 44 marks, Yogesh got 55 marks, Saurav got 66 marks, Kerikeri got 77 marks,and Abhijit got 88 marks"
namelist=re.findall("[A-Z][a-z]+",gd)
print("*"*50)
print("Name Of Students")
print("*"*50)
for name in namelist:
    print("\t{}".format(name))
print("*"*50)




