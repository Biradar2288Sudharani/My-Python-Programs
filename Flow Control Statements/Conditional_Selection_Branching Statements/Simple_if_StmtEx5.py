# WAPP which will accept three numerical values & decide Smallest among them & check for equality by using simple if statement
# Simple_if_StmtEx5.py
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if((a<b)and(a<c)):
    print("Smallest Number ({},{},{})={}".format(a,b,c,a))
if((b<a)and(b<c)):
    print("Smallest Number ({},{},{})={}".format(a,b,c,b))
if((c<a)and(c<b)):
    print("Smallest Number ({},{},{})={}".format(a,b,c,c))
if((a==b)and(b==c)):
    print("All Numbers Are Equal")
print("Program Execution Is Completed!!")


















