# SharesDemo.py
import Shares
import time 
import importlib
def disp(d):
    print("*"*50)
    print("\t Shares Name \t Value")
    print("*"*50)
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
    else:
        print("*"*50)


# Main Program
d=Shares.sharesinfo()
disp(d)
time.sleep(10)
importlib.reload(Shares)  # Reloading previously importing module.
d=Shares.sharesinfo()  # Obtaining changed / new values of previously imported module.
disp(d)





