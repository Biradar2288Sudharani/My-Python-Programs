# DivEx3.py
# WAPP for accepting two integer value and find their division with handling exception.
try:
    s1=input("Enter first value:")
    s2=input("Enter second value:")
    a=int(s1)
    b=int(s2)
    c=a/b
except (ZeroDivisionError,ValueError):
    print("Don't Enter Zero By Denominator!")
    print("\tDon't Enter alnums,strs,and special symbols by denominato!!")
else:
    print("*"*50)
    print("First Value:{}".format(a))
    print("Second Value:{}".format(b))
    print("Div={}".format(c))
    print("*"*50)
finally:
    print("I am from finally block!")


''' --> ANSWER <--
Enter first value:12
Enter second value:2
First Value:12
Second Value:2
Div=6.0
**************************************************
First Value:12
Second Value:2
Div=6.0
**************************************************
I am from finally block!
'''










