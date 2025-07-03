# WAPP which will calculate factorial of given number.
# WhileLoopEx11.py
n=int(input("Enter a number for finding a factorial:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    f=1
    i=1
    while(i<=n):
        f=f*i
        i=i+1
    else:
        print("Factorial ({})={}".format(n,f))

# REVERSE CONCEPT OF FACTORIAL:
n=int(input("Enter a number for finding a factorial:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    f=1
    i=n
    while(i>0):
        f=f*i
        i=i-1
    else:
        print("\t {}!".format(n,f))

# --> OR <--
import math
print(math.factorial(5))















