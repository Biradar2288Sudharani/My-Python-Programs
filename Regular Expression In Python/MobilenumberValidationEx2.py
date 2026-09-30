# MobilenumberValidationEx2.py
# WAPP which will validating mobile number.
# Doubt in this program
# Logic 1
import re
while(True):
    mno=input("Enter your mobile number:")
    if (len(mno)==10):
        res=re.search(r"[98]\d{8}",mno)
        if(res!=None):
            print("\t{} is a valid mobile number")
            break
        else:
            print("Mobile Number Shouldn't Be Non-Int----Try Again!!!")
    else:
        print("\t{} is invalid length mobile number----Try Again!!!")


# Logic 2
import re
while(True):
    mno=input("Enter your mobile number:")
    if (len(mno)==10):
        res=re.search(r"(98)\d{8}",mno)
        if(res!=None):
            print("\t{} is a valid mobile number")
            break
        else:
            print("Mobile Number Shouldn't Be Non-Int----Try Again!!!")
            break
    else:
        print("\t{} is invalid length mobile number----Try Again!!!")