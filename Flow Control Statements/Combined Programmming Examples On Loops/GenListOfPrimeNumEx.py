# program for generating list of prime numbers within the range of n where n is positive. 
# PrimeNumEx.py
n=int(input("Enter the rage for listing the primes:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    print("List of Primes within: {}".format(n))
    for num in range(2,n+1):   # Outer Loop
        res=True
        for i in range(2,num): # Inner Loop
            if(num%i==0):
                res=False
                break
            if(res):
                print("\t{}".format(res))









