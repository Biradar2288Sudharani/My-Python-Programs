# WAPP which will accept list of values and find their sum and average
# BreakEx6.py
# Logic 1
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
        s=0
        for val in lst:
            print("\t{}".format(val))
            s=s+val
        else:
            print("\t Sum({})={}".format(lst,s))
            print("\t Average={}".format(s/len(lst)))

# Logic 2
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
# code for finding sum and average
print("\t Sum({})={}".format(lst,s))
print("\t Average={}".format(s/len(lst)))



