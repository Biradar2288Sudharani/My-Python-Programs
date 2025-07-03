# WAPP which will generate all the even numbers,within n in forword direction where n can be positive. 
# WhileLoopEx3.py
n=int(input("Enter how many Number you want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    # loop logic for generating 1 to n number
    i=2 # Initilize Part
    while(i<=n):  # Test Condition
        print("{}".format(i))
        i=i+2   # Updation Part
    else:
        print("I am from else-part of while loop")
print("Program Execution Completed!!!!")



















