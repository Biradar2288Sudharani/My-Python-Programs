# SampleEx1.py
# Program for demonstrating sample().
import random as r
print("*"*50)
captcha="ABCDEFGHIJKLMNOPQRSTUVWXYZ1,2,3,4,5,6,7,8,9ancdefghijklmnopqrstuvwxyz!@#$%^&*()+=-><?/\|]["
for i in range(1,11):
    print(r.sample(captcha,k=6))

print("*"*50)
captcha="ABCDEFGHIJKLMNOPQRSTUVWXYZ1,2,3,4,5,6,7,8,9ancdefghijklmnopqrstuvwxyz!@#$%^&*()+=-><?/\|]["
for i in range(1,11):
    print(" ".join(r.sample(captcha,k=6)))
print("*"*50)




