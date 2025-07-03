# WAPP which will accept any value from keyboard & display whether it is alphabet or digit or alphanumeric by using if-else statement.
# if-elseStmtEx3.py
# My Logic
a=input("Enter any value from keyboard:")
if(a.isalpha()):
    print(" Given value {} is Alphabet".format(a))
if(a.isdigit()):
    print(" Given value {} is Digit".format(a))
if(a.isalnum()):
    print(" Given value {} is AlphaNumeric".format(a))
else:
    print("Entering value from keyboard is not digit,not alphabet and  not alphanumeric")

# OR----->("KVR Sir Logic")
val=input("Enter any value from keyboard:")
if(val.isalpha()):
    print("Given value {} is Alphabet".format(val))
else:
    if(val.isdigit()):
        print("Given value {} is Digit".format(val))
    else:
        if(val.isalnum()):
            print("Given value {} is AlphaNumeric".format(val))
        else:
            print("Entering value from keyboard is not digit,not alphabet and  not alphanumeric")













