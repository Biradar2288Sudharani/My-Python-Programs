# RegularExpressionEx12.py
# Program for searching for all digits.
import re
sp="[abc]"
matres=re.finditer("[0-9]" , "CH2a31b42c636e@u#uTrRrS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)