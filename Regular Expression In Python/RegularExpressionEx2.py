# RegularExpressionEx2.py
import re
gd="Python is an oops language. python is also functional language."
sp="Python"
matres=re.search(sp,gd)
if (matres!=None):
    print("Search is Successful!!!")
    print("Start Index",matres.start())
    print("End Index",matres.end())
    print("Matched Values:", matres.group())
else:
    print("Search is Not Successful!!!")


