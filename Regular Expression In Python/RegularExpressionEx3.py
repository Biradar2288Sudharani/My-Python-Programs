# RegularExpressionEx3.py
import re
gd="Python is an oops language. python is also functional language."
sp="Python"
noc=0
matres=re.finditer(sp,gd)
for i in matres:
    print("Start Inadex:{} End Index:{} Value:{}".format(i.start(),i.end(),i.group))
    noc=noc+1
    print("Number of Occurance of {}={}".format(sp,noc))


