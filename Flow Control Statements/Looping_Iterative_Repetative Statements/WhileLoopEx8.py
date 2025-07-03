# WAPP which will calculate sum of squares of n natural numbers.
# WhileLoopEx8.py
n=int(input("Enter how many natural number squares sum you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Numbers Within:{}".format(n))
    i=1
    s=0
    ss=0
    while(i<=n):
        print("\t\t {} \t\t\t\t {}".format(i,i**2))
        s=s+i
        ss=ss+i**2
        i=i+1
    else:
        print("\t\t {} \t\t\t\t {}".format(s,ss))

'''
Here s=sum
     ss=square sum
'''















