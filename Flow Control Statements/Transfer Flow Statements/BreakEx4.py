# WAPP which will accept any numerical integer value & decide whether it is prime or not
# BrealEx4.py
# Logic 1
n=int(input(" Enter a Number:"))
if(n<=1):
    print("{} Is Invalid Input".format(n))
else:
    res="prime"
    for i in range(2,n):
        if(n%i==0):
            res="not prime"
            break
        if(res=="prime"):
            print("{} is prime".format(n,res))
        else:
            print("{} is not prime".format(n,res))


# Logic 2
n=int(input(" Enter a Number:"))
if(n<=1):
    print("{} Is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
        if(res):
            print("{} Is Prime".format(n))
    else:
        print("{} Is Not Prime".format(n))






