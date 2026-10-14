# OtherProgram3.py
from Account2 import account
ac=account()  # Object Creation----Makes the PVM to call default constructor.
print(ac.__dict__)
ac.getaccdetails()
print("Account Holder Number=",ac.acno)
print("Account Holder Name=",ac.cname)
print("Account Holder Balance=",ac.bal)
print("Account Holder Pin=",ac.pin)
print("Account Holder Branch Name=",ac.bnmae)