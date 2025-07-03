# UniformEx.py
import random as r
print("*"*50)
for i in range(1,6):
    print(r.uniform(2,2.5))
print("----- OR -----")
for i in range(1,6):
    print("%0.2f"%r.uniform(10.5,11.5))
print("----- OR -----")
for i in range(1,6):
    print("{}".format(round(r.uniform(100,101),3)))
print("*"*50)