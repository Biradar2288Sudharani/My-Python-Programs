# RegularExpressionEx1.py
# Program for searching a word.
import re
gd="Python is an oops language. python is also functional language."
sp="Python"
result=re.findall(sp,gd)
print("Number of Occurance of {}={}".format(sp,len(sp)))




