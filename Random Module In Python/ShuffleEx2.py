# ShuffleEx2.py
# Program for demonstrating shuffle().
import random as r
print("*"*50)
s="MISSISSIPPI"
ls=list(s)
for i in range(1,len(ls)+1):
    r.shuffle(ls)
    print("".join(ls))
print("*"*50)




