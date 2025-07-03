# WAPP which will calculate factorial of given number by using for loop.
# ForLoopEx5.py
n=int(input("Enter a number for finding a factorial:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    else:
        print("\t{}!={}".format(n,f))