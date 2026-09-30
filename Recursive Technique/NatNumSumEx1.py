# program for adding first N natural numbers by using recursion
# NatNumSumEx.py
def natsum(n):
    print("\t{}".format(n))
    if(n==0):
        return 0
    else:
        return(n+natsum(n-1)) #recursive fumction
#main program
n=int(input("Enter how many numbers sum you want to find:"))
if(n<0):
    print("{} Is Invali Input".format(n))
else:
    res=natsum(n)
    print("Natural Number Sum({})={}".format(n,res))
