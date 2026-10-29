# EqualityCheckEx.py
# WAPP which will accept two numerical values and find the biggest and check for their equalityby using anonymous function.
findbig=lambda a,b:a if a>b else b if b>a else "All values are equal"
# Main Program
a,b=float(input("Enter value of a:")),float(input("Enter value of b:"))
res=findbig(a,b)
print("Big({},{})={}".format(a,b,res)) 








