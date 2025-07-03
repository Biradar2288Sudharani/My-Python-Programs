#program for calculate factorial for given number
#RecursiveFactEx2.py
def fact(n):
    if(n==0):
        return 1
    else:
        return(n*fact(n-1)) #recursive function call
    
def Calculation(n):
    res=fact(n)
    print("Fact({})={}".format(n,res))

#main program
n=int(input("Enter a number for calculate given number"))
if(n<0):
    print("{} Is Invalid input".format(n))
else:
    Calculation(n)
    