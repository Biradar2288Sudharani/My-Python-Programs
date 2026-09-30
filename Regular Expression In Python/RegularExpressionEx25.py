# RegularExpressionEx25.py
# Program for searching exactly zero k or one k.
import re
sp="[abc]"
matres=re.finditer("k?" , "kkvvrrkkvvvvrrkkkdssd")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)