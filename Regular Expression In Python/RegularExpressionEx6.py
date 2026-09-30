# RegularExpressionEx6.py
# Program for searching uppper case alphabets
import re
sp="[abc]"
matres=re.finditer("[A-Z]" , "CH123@#TRS")
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)












