# FundsTransferApplications.py
''' --> QUESTION <--
WAPP which will implement the following some of the operations of ATM. and develop hit 
and handle the appropriate exceptions.
-----------------------------------------------------
ATM Operations OR Funds Transfer Applications :
-----------------------------------------------------
           1. Deposite
           2. Withdraw
           3. Balance Enquiry
           4. Exit
-----------------------------------------------------
File System :
-----------------------------------------------------
              1. AtmMenu.py
              2. AtmOperations.py
              3. AtmExcept.py
              4. AtmMainPro.py
'''

import sys
def menu():
    print("*"*50)
    print("\tATM or Funds Transfer Application")
    print("*"*50)
    print("\t1.Deposite")
    print("\t2. Withdraw")
    print("\t3. Balance Enquiry")
    print("\t4. Exit")
    print("*"*50)

class DepositeError(Exception):pass

class WithdrawError(BaseException):pass

class InsufficientFundError(Exception):pass

bal=500.00  # Here bal is global variable
def deposite():
    damt=float(input("Enter the deposite amount:"))
    if(damt<=0):
        raise DepositeError
    else:
        global bal
        bal=bal+damt
        print("Your Account xxxxxxxx123 Credited With INR:{}".format(damt))
        print("Now Your Account xxxxxxxx123 Bal After Deposite INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter the withdraw amount:"))  # Implicitely their is an exception --- ValueError
    if(wamt<=0):
        raise WindowsError
    elif((wamt + 500)>bal):
        raise InsufficientFundError
    else:
        bal=bal-wamt
        print("Your Account xxxxxxx123 Debited With INR:{}".format(wamt))
        print("Your account xxxxxxx123 Bal After Withdraw INR:{}".format(bal))

def balenquiry():
    print("Your Balance In Account xxxxxxx123 INR:{}".format(bal))

while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposite()
                except DepositeError:
                    print("Don't Enter Negative or Zero From Deposite Amount")
                except ValueError:
                    print("Don't Try To Deposite alnums,strs and symbols For Depositing Amount")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Don't Enter Negative or Zero From Deposite Amount")
                except InsufficientFundError:
                    print("Your account doesn't have sufficient balance or funds")
                except ValueError:
                    print("Don't Try To Deposite alnums,strs and symbols For Depositing Amount")
            case 3:
                balenquiry
            case 4:
                print("Thanks For Using This Program")
                sys.exit
            case _:
                print("Your Selection Of Operation Wrong---Try Again")
    except ValueError:
        print("Don't Try To Deposite alnums,strs and symbols For Depositing Amount")
































