# booean examples
a=True
print(a,type(a))
a=False
print(a,type(a))

# in boolean condsider the True as 1 and False as 0 or (boolean arithmetic opertations) on their examples
a=True
b=False
c=a+b
print(c)
print(4*True+2+True)
print(0b1111*True-True)
print(False/True)
print(True-0xF*2)
print(True+0xf*2)
true=True
false=False
print(true+false-True)


# boolean errors
a=true
print(a,type(a))           #.............NameError
a=false
print(a,type(a))           #.............NameError
print(True/False)          #............ZeroDivisionError
