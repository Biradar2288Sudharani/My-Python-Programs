# SampleEx2.py
import random as r
print("*"*50)
sc=["KA","TC","AP","MH"]
sd=["08","09","32","07"] 
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0,1,2,3,4,5,6,7,8,9"
for i in range(1,21):
    s1=r.sample(sc,1)
    s2=r.sample(sd,1)
    s3=r.sample(alpha,2)
    s4=r.sample(digits,4)
    numplate=" ".join(s1)+" "+" ".join(s2)+" "+" ".join(s3)+" "+" ".join(s4)

print("\t\t{}".format(numplate))
print("*"*50)



