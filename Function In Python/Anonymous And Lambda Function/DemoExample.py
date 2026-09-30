# DemoExample.py
def sumop(a,b):
    c=a+b 
    return c
# Main Program
print("By Using Normal Function")
print("Type of Sumop=",type(sumop))
res=sumop(2003,3221)
print("Sum By Using Normal Function=",res)
print("*"*50)

addop=lambda k,v:k+v
# Main Program
print("By Using Anonymous Function")
print("Type of Addop=",type(addop))
res=sumop(2003,3221)
print("Sum By Using Anonymous Function=",res)
print("*"*50)





