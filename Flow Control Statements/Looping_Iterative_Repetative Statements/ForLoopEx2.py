# WAPP which will generate all the even numbers by using for loop where n can be positive. 
# ForLoopEx2.py
n=int(input("Enter how many Number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Even Numbers Within in : {}".format(n))
    for i in range(2,n+1,2):
        print("\t\t {}".format(i))


















