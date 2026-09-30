#program for calculate factorial for given number
#UsingLoopsFact.py
def fact(n):
    f=1
    if(n==0):
        return f
    else:
        for i in range(1,n+1):
            f=f*i
        return f
#main program
n=int(input("Enter a number for calculate given number:"))
if(n<0):
    print("{} Is Invalid input".format(n))
else:
    res=fact(n)  #Normal function call
    print("Fact({})={}".format(n,res))