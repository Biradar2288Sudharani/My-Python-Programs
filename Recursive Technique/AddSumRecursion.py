def addop(a,b):
    if(b==0):
        return a
    else:
        return(addop(a+1 , b-1))
#main program
print("Enter Two values")
a,b=int(input()),int(input())
if(b<a):
    print("Invalid Input")
else:
    res=addop(a,b) #function call
    print("Sum({},{})={}".format(a,b,res))