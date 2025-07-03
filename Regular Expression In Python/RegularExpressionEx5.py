# RegularExpressionEx5.py
# Program for searching either 'a' or 'b' or 'c'
import re
gd="CHa3TbPQrstuX@#"
sp="[abc]"
matres=re.finditer(sp,gd)
print("*"*50)
for i in matres:
    print("\t Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
print("*"*50)



