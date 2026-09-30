# RandomEx.py
import random as r
print("*"*50)
for i in range(1,6):
    print(r.random())
print("----- OR -----")
for i in range(1,6):
    print("%0.2f"%r.random())
print("----- OR -----")
for i in range(1,6):
    print("{}".format(round(r.random(),3)))
print("*"*50)




