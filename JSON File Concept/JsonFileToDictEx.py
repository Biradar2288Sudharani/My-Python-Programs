# JsonFileToDictEx.py
# To read the json file data into dict object , we use json.load(File Pointer).
import json
try:
    with open("student.json","r") as fp:
        dobj=json.load(fp)
        print("*"*50)
        for k,v in dobj.items():
            print("\t{}-->{}".format(k,v))
        print("*"*50)

except FileNotFoundError:
    print("JSON File Not Exist!!!")














