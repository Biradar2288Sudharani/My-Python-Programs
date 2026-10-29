# NormalAndAnonymousFunEx.py
# By Using Normal Function
def sumop(a,b):
    c=a+b
    return c
# Main Program
print("Type Of Sumop=",type(sumop))
res=sumop(100,200)
print("sum=",res)

# By Using Anonymous Function
addop=lambda a,b : a+b
# Main Program
print("Type Of Sumop=",type(sumop))
res=sumop(200,500)
print("sum=",res)

