# WAPP which will calculate sum of two numbers by using Functions.
# Approch Number 1 Example.py
def addop(k,v):   # Function Defination
    r=k+v  # Here r is called local variable
    return r
# main program
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
res=addop(a,b)   # Function Call
print("Sum ({},{})={}".format(a,b,res))
print("*"*10)
k=float(input("Enter value of k:"))
v=float(input("Enter value of v:"))
r=addop(k,v)   # Function Call
print("{}+{}={}".format(k,v,r))








