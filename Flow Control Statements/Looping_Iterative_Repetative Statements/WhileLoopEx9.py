# WAPP which will calculates sum of cubes of n natural numbers
# WhileLoopEx9.py
n=int(input("Enter how many natural number cubes sum you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Numbers Within:{}".format(n))
    i=1
    s=0
    cs=0
    while(i<=n):
        print("\t\t {} \t\t\t\t {}".format(i,i**3))
        s=s+i
        cs=cs+i**2
        i=i+1
    else:
        print("\t\t {} \t\t\t\t {}".format(s,cs))

'''
Here s=sum
     cs=cube sum
'''


















