# WAPP which will accept two numerical values & decide the smallest among them & check for equality
# TernaryOperatorEx2.py
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
s=b if b<a else a
print("Small ({},{})={}".format(a,b,s))
S=a if a<b else b if b<a else "both values are equal"
print("Small ({},{})={}".format(a,b,S))
