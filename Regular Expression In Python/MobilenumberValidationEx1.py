# MobilenumberValidationEx1.py
# WAPP which will validating mobile number.
import re
while(True):
    mno=input("Enter your mobile number:")
    if (len(mno)==10):
        res=re.search(r"\d{10}",mno)
        if(res!=None):
            print("\t{} is a valid mobile number")
            break
        else:
            print("Mobile Number Shouldn't Be Non-Int----Try Again!!!")
    else:
        print("\t{} is invalid length mobile number----Try Again!!!")



