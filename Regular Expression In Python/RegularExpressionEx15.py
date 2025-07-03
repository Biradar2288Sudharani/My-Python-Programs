# RegularExpressionEx14.py
# Program for searching for all except digits.
import re
sp="[abc]"
matres=re.finditer("[^0-9]" , "CHa1b2c3e@u#uTrRrS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)