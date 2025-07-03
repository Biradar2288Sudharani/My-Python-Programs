# WAPP which will accept sum of n natural numbers where n is positive.
# WhileLoopEx7.py
n=int(input("Enter how many natural numbers sum you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Numbers Within:{}".format(n))
    i=1
    p=0
    while(i<=n):
        p=p+i
        print("\t".format(i))
        i=i+1
        print(i)
    else:
        print("Sum of {} Natural Numbers={}".format(n,p))













