# WAPP which will generate n to 1, where n is positive integer value.
# WhileLoopEx2.py
n=int(input("Enter how many number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    # loop logic for generating 1 to n number
    i=n # Initilize Part
    while(i>=1):  # Test Condition
        print("{}".format(i))
        i=i-1   # Updation Part
    else:
        print("I am from else-part of while loop")
print("Program Execution Completed!!!!")



















