# WAPP which will accept list of values and display them.
# BreakEx5.py
n=int(input("Enter how many values you want to enter:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} Number:".format(i)))
        lst.append(val)
    else:
        print("Given List Of Values={}".format(lst))
        







