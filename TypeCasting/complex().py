# SYNTAX : varname(int|float|bool|str)

#EXAMPLE-1: int type into complex type--------POSSIBLE
a=3
print(a,type(a))
b=complex(a)
print(b,type(b))


#EXAMPLE-2: float type into complex type--------POSSIBLE
a=3.14
print(a,type(a))
b=complex(a)
print(b,type(b))

#EXAMPLE-3: bool type into complex type-------- POSSIBLE
a=True
print(a,type(a))
b=complex(a)
print(b,type(b))

a=False
print(a,type(a))
b=complex(a)
print(b,type(b))

#EXAMPLE-4: str type into complex type
#CASE - 1 : str int into complex ---------POSSIBLE
a="10"
print(a,type(a))
b=complex(a)
print(b,type(b))

#CASE - 2 : str float into complex ---------POSSIBLE
a="10.98"
print(a,type(a))
b=complex(a)
print(b,type(b))

'''
#CASE - 3 : str bool into complex ---------NOT POSSIBLE
a="True"
print(a,type(a))
b=complex(a)
print(b,type(b))
'''
      
#CASE - 4 : str complex into complex ---------POSSIBLE
a="10+12j"
print(a,type(a))
b=complex(a)
print(b,type(b))

'''
#CASE - 5 : pure str into complex ---------NOT POSSIBLE
a="python"
print(a,type(a))
b=complex(a)
print(b,type(b))
'''

