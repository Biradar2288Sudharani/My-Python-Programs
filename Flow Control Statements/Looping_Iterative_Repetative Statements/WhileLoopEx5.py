# WAPP which will generate even numbers in backword direction from n where n is positive integer value.
# WhileLoopEx5.py
n=int(input("Enter how many numbers want to generate in backward direction:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Even Number From {} to {}".format(n,2))
    if(n%2!=0):
        n=n-1
    i=n
    while(i>=2):
        print("\t\t {} ".format(i))
        i=i-2




















