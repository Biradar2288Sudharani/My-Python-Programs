# DictToJsonFileEx.py
import json
d1={"sno":"100","sname":"sudha"} # Here d1 is an object of <class,'dict'>
# We can save dict object data into file by using a predefined function called json.dump(object,file pointer).
with open("Student.json","r") as fp:
    json.dump(d1,fp)
    print("Dict data saved in JSON File!!!")





