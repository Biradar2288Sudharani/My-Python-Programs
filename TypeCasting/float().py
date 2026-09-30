# SYNTAX : varname(int|bool|complex|str)

#EXAMPLE-1: int type into float type--------POSSIBLE
a=134
print(a,type(a))
b=float(a)
print(b,type(b))

#EXAMPLE-2: bool type into float type--------POSSIBLE
a=True
print(a,type(a))
b=float(a)
print(b,type(b))

a=False
print(a,type(a))
b=float(a)
print(b,type(b))

'''
#EXAMPLE-3: complex type into float type--------NOT POSSIBLE
a=2+3j
print(a,type(a))
b=float(a)
print(b,type(b)).............VALUE ERROR
'''

#EXAMPLE-4: str type into int type
#CASE - 1 : str int into float ---------POSSIBLE
a="234"
print(a,type(a))
b=float(a)
print(b,type(b))



#CASE - 2 : str float into float ---------POSSIBLE
a="2.22"
print(a,type(a))
b=float(a)
print(b,type(b))

'''
#CASE - 3 : str bool into float ---------NOT POSSIBLE
a="True"
print(a,type(a))
b=float(a)
print(b,type(b)).............VALUE ERROR
'''

'''
#CASE - 4 : str complex into float ---------POSSIBLE
a="2+3j"
print(a,type(a))
b=float(a)
print(b,type(b)).............VALUE ERROR
'''

'''
#CASE - 5 : pure str into float ---------POSSIBLE
a="SUDHARANI"
print(a,type(a))
b=float(a)
print(b,type(b)).............VALUE ERROR
'''











