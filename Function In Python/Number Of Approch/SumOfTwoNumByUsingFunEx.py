# WAPP which will calculate sum of two numbers by using Functions.
# SumOfTwoNumByUsingFunEx.py
def sumop(a,b):  # Here a and b are formal parameter
    print("I am inside the function defination...")
    c=a+b  # Here c is local variable
    return c

# Main Program
print("Program Execution Starts")
r=sumop(10,20)  # Function Call
print("Sum=",r)
print("*"*5)
res=sumop(100,200)  # Function Call
print("Sum=",res)
print("Program Execution Ends")
print("Type Of Sum=",type(sum))





















