# DivEx3.py
# WAPP for accepting two integer value and find their division with handling exception.
try:
    s1=input("Enter first value:")
    s2=input("Enter second value:")
    a=int(s1)
    b=int(s2)
    print("First Value:{}".format(a))
    print("Second Value:{}".format(b))
    c=a/b
    print("Div={}".format(c))
except ZeroDivisionError:
    print("Don't Enter Zero By Denominator!")
except ValueError:
    print("\tDon't Enter alnums,strs,and special symbols by denominato!!")
else:
    print("*"*50)
    print("First Value:{}".format(a))
    print("Second Value:{}".format(b))
    print("Div={}".format(c))
    print("*"*50)
finally:
    print("I am from finally block!")













