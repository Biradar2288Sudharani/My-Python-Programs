# WAPP which will accept two integer values & find biggest among them 
# if-elseStmtEx1.py
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if(a>b):
    print("Biggest Number ({},{})={}".format(a,b,a))
else:
    print("Biggest Number ({},{})={}".format(a,b,b))
print("Program Execution Is Completed!!")

# OR----
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if(a>b):
    print("Biggest Number ({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("Biggest Number ({},{})={}".format(a,b,b))
    else:
        print("BOth values are equal!!!!!!")
        
print("Program Execution Is Completed!!")









