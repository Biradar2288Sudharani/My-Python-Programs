# AtmMainPro.py
from AtmMenu import menu
from AtmExcept import DepositeError,WithdrawError,InsufficientFundError
from AtmOperations import deposite,withdraw,balenquiry
import sys
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









