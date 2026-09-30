# program for power pf a certain number by using recursion
#PowerOfNumberEx.py
def respow(b,p):
    if(p==0):
        return 1
    else:
        return(b*respow(b,p-1)) #recursive function
# main program 
b,p=int(input("Enter Base:")),int(input("Enter Power:"))
if(p>0):
    res=respow(b,p)
    print("Power ({},{})={}".format(b,p,res))
else:
    res=b**p
    print("Power ({},{})={}".format(b.p,res))
