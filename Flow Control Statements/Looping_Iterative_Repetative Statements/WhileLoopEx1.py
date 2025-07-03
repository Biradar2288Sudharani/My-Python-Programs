# WAPP which will generate one to n numbers by using loops.
# WhileLoopEx1.py
n=int(input("Enter how many number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    # loop logic for generating 1 to n number
    i=1 # Initilize Part
    while(i<=n):  # Test Condition
        print("{}".format(i))
        i=i+1   # Updation Part
    else:
        print("I am from else-part of while loop")
print("Program Execution Completed!!!!")















