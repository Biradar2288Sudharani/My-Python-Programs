# JsonFmtToDictEx.py
import json
jsonfmt='{"sno":"100","sname":"sudha"}'
print("Type of jsonfmt={}".format(type(jsonfmt)))
# Convert JSON data into dict type....use a pre-defined function called json.loads(json data).
dobj=json.loads(jsonfmt)
print("Type of jsonfmt={}".format(type(dobj)))
for k,v in dobj.items():
    print("\t{}-->{}".format(k,v))






