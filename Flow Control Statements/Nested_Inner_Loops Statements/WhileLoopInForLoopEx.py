# WhileLoopInForLoopEx.py
for i in range(1,6):  # Outer Loop
    print("Inner Loop-->i={}".format(i))
    j=1
    while(j<=6): # Inner Loop
        print("\t\tInner Loop-->j={}".format(j))
        j=j+1
    else:
        print("-----")
else:
    print()