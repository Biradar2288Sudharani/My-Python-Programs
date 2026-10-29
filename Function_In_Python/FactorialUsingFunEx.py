# WAPP which will accept any numerical value and calculate it's factorial by using functio.
# FactorialUsingFunEx.py
def fact(n):
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
            print("Factorial ({}!)={}".format(n,f))

# Main Program
fact(fact)















