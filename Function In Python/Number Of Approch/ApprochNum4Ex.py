# WAPP which will calculate sum of two numbers by using Functions.
# Approch Number 3 Example.py 
def sumop():
    # Input
    k=float(input("Enter value of k:"))
    v=float(input("Enter value of v:"))
    # Process 
    r=k+v
    # give result to function call
    return k,v,r   # Return statement not only returns one value but also more number values
# Main Program
res=sumop()  # Function call in single line assignment
print("Sum({},{})={}".format(k,v,res))
a,b,c=sumop()   # Function call in multiple assignment
print("Sum({},{})={}".format(a,b,c))
res=sumop()   # Here res is type of <class 'Tuple'>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
print("---> OR <---")
print("Sum({},{})={}".format(res[-3],res[-2],res[-1]))
print("---> OR <---")
print("Sum({},{})={}".format(res[0:1],res[1:2],res[2:]))








