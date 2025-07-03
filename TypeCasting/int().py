# SYNTAX : varname(float|bool|complex|str)

#EXAMPLE-1: float type into int type--------POSSIBLE
a=3.14
print(a,type(a))
b=int(a)
print(b,type(b))
print(int(100.99))
print(int(0.0))

#EXAMPLE-2: bool type into int type--------POSSIBLE
a=True
print(a,type(a))
b=int(a)
print(b,type(b))

a=False
print(a,type(a))
b=int(a)
print(b,type(b))

'''
#EXAMPLE-3: complex type into int type-------- NOT POSSIBLE
a=2+3j
print(a,type(a))
b=int(a)
print(b,type(b))
'''

#EXAMPLE-4: str type into int type
#CASE - 1 : str int into int ---------POSSIBLE
a="12"
print(a,type(a))
b=int(a)
print(b,type(b))

'''
#CASE - 2 : str float into int ---------NOT POSSIBLE
a="12.34"
print(a,type(a))
b=int(a)
print(b,type(b))...............VALUE ERROR
'''

'''
#CASE - 3 : str bool into int ---------NOT POSSIBLE
a="True"
print(a,type(a))
b=int(a)
print(b,type(b)).............VALUE ERROR
'''

'''
#CASE - 4 : str complex into int ---------NOT POSSIBLE
a="12+15j"
print(a,type(a))
b=int(a)
print(b,type(b)).............VALUE ERROR
'''

'''
#CASE - 5 : pure str into int ---------NOT POSSIBLE
a="SUDHARANI"
print(a,type(a))
b=int(a)
print(b,type(b))............VALUE ERROR
'''
