# RegularExpressionEx10.py
# Program for searching for all alphabets
import re
sp="[abc]"
matres=re.finditer("[A-Za-z]" , "CHa1b2c3e@u#uTrRrS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)