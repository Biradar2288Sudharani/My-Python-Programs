# SamllestValueEx.py
# WAPP which will accept two numerical values and find the smallest and check for their equalityby using anonymous function.
findsmall=lambda a,b:a if a<b else b if b<a else "Both values are equal"
# Main Program
a,b=float(input("Enter value of a:")),float(input("Enter value of b:"))
res=findsmall(a,b)
print("Big({},{})={}".format(a,b,res))