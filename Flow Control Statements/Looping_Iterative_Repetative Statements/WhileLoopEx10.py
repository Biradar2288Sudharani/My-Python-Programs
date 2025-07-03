# WAPP which will calculate product of n natural numbers.
# WhileLoopEx10.py
n=int(input("Enter how many natural number product you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Number {}".format(n))
    i=1
    p=1
    while(i<=n):
        print("\t\t{}".format(i))
        p=p*i
        i=i+1
    else:
        print("Product of {} Natural Number={}".format(n,p))










