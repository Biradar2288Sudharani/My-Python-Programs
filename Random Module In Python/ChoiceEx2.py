# ChoiceEx2.py
import random as r
alphas="ABCDEFGHIJKLMNOPQRSTUVWXYZancdefghijklmnopqrstuvwxyz"
digits="1,2,3,4,5,6,7,8,9"
symbols="!@#$%^&*()+=-><?/\|]["
for i in range(1,11):
    print(r.choice(alphas),r.choice(digits),r.choice(symbols))
print("*"*50)
captcha="ABCDEFGHIJKLMNOPQRSTUVWXYZ1,2,3,4,5,6,7,8,9ancdefghijklmnopqrstuvwxyz!@#$%^&*()+=-><?/\|]["
for i in range(1,11):
    print(r.choice(captcha)+r.choice(captcha)+r.choice(captcha)+r.choice(captcha)+r.choice(captcha)+r.choice(captcha))
print("*"*50)




