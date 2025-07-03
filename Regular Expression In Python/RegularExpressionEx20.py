# RegularExpressionEx20.py
# Program for searching for all word characters.
import re
sp="[abc]"
matres=re.finditer(r"\w" , "CHa1b2c 3e@ u#uTrRrS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)