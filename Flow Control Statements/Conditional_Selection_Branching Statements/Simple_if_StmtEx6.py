# WAPP which will accept any value from keyboard & display whether it is alphabet or digit or alphanumeric
# Simple_if_StmtEx6.py
a=input("Enter any value from keyboard:")
if(a.isalpha()):
    print(" Given value {} is Alphabet".format(a))
if(a.isdigit()):
    print(" Given value {} is Digit".format(a))
if(a.isalnum()):
    print(" Given value {} is AlphaNumeric".format(a))
# print("Entering value from keyboard is not digit,not alphabet and  not alphanumeric") 