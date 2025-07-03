# ForLoopInWhileEx.py
# Example 1
i=1
while(i<=5):  # Outer Loop
    print("Outer Loop--i={}".format(i))
    print("-------")
    for j in range(1,10):  # Inner Loop
        print("\t\tInner Loop-->j={}".format(j))
    else:
        i=i+1
        print("-------")
else:
    print()
        
# Example 2
i=1
while(i<=5):  # Outer Loop
    print("Outer Loop--i={}".format(i))
    print("-------")
    for j in range(1,10):  # Inner Loop
        print("\t\tInner Loop-->j={}".format(j))
    else:
        i=i-1
        print("-------")
else:
    print()















