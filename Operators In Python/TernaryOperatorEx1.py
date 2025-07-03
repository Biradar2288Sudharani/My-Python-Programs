# WAPP which will accept two numerical values & decide the biggest among them & check for equality
# TernaryOperatorEx1.py
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
s=b if b>a else a
print("Big ({},{})={}".format(a,b,s))
S=a if a>b else b if b>a else "both values are equal"
print("Big ({},{})={}".format(a,b,S))













