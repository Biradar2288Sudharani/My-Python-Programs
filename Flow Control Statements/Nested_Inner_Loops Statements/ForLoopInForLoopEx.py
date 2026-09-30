# ForLoopInForLoopEx.py
# Example 1
for i in range(1,6):  # Outer Loop
    print("Inner Loop-->i={}".format(i))
    for j in range(1,4):  # Inner Loop
        print("\t\tInner Loop-->j={}".format(j))

# Example 2
for i in range(1,4):
    print("\t\t i \t\t j \t\t k")
    for j in range(1,4):
        for k in range(1,4):
            print("\t\t {} \t\t {} \t\t {}".format(i,j,k))
        else:
            print("------------")
    





















