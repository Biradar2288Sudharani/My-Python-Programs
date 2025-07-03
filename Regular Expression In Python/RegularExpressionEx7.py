# RegularExpressionEx7.py
# Program for searching for all except uppper case alphabets
import re
sp="[abc]"
matres=re.finditer("[^A-Z]" , "CH123@#TRS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)