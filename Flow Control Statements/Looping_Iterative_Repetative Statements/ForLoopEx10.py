# WAPP which will accept any number and finding its factors.
# ForLoopEx10.py
# Input: Given Number 24
# Expected Output:1 2 3 4 6 8 12
n=int(input("Enter a number for finding a factorial:")) 
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):  # for i in range(1,n//2+2)
        if(n%i==0):
            print(i)














