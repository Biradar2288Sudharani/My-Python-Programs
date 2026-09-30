# WAPP which will accept three numerical values and find the biggest among them and check for equality
# TernaryOperatorEx4.py
# Logic 1
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
reversed=a if (a>b) and (a>c) else b if (b>a) and (b>c) else c if (c>a) and (c>b) else "all are equal"
print("Big ({},{},{})={}".format(a,b,c,reversed))

# Logic 2
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
reversed=a if (a>=b) and (a>c) else b if (b>=a) and (b>c) else c if (c>=a) and (c>b) else "all are equal"
print("Big ({},{},{})={}".format(a,b,c,reversed))














