# WhileLoopInWhileLoopEx.py
i=1
while(i<=5):  # Outer Loop
    print("Outer Loop--i={}".format(i))
    j=1
    while(j<=6): # Inner Loop
        print("\t\tInner Loop-->j={}".format(j))
        j=j+1
    else:
        i=i+1
        print("#"*20)
else:
    print()
    
    















