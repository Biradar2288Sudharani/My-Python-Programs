# WAPP which will accpt any three numerical values & find smallest among them & check for equality
# TernaryOperatorEx5.py
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
reversed=a if (a<b) and (a<c) else b if (b<a) and (b<c) else c if (c<a) and (c<b) else "all are equal"
print("Small ({},{},{})={}".format(a,b,c,reversed))

# Logic 2
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
reversed=a if (a<=b) and (a<c) else b if (b<=a) and (b<c) else c if (c<=a) and (c<b) else "all are equal"
print("Small ({},{},{})={}".format(a,b,c,reversed))























