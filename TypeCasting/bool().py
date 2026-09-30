# SYNTAX : varname(int|float|complex|str)

#EXAMPLE-1: int type into bool type--------POSSIBLE
a=10
print(a,type(a))
b=bool(a)
print(b,type(b))

a=0
print(a,type(a))
b=bool(a)
print(b,type(b))

#EXAMPLE-2: float type into bool type--------POSSIBLE
a=3.14
print(a,type(a))
b=bool(a)
print(b,type(b))


#EXAMPLE-3: complex type into bool type-------- POSSIBLE
a=3+4j
print(a,type(a))
b=bool(a)
print(b,type(b))

a=0+0j
print(a,type(a))
b=bool(a)
print(b,type(b))

#EXAMPLE-4: str type into bool type
#CASE - 1 : str int into bool ---------POSSIBLE
a="123"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="0"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="000000"
print(a,type(a))
b=bool(a)
print(b,type(b))

#CASE - 2 : str float into bool ---------POSSIBLE
a="3.14"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="0.0"
print(a,type(a))
b=bool(a)
print(b,type(b))

#CASE - 3 : str bool into bool ---------POSSIBLE
a="True"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="False"
print(a,type(a))
b=bool(a)
print(b,type(b))

#CASE - 4 : str complex into bool ---------POSSIBLE
a="2+3j"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="0+0.0j"
print(a,type(a))
b=bool(a)
print(b,type(b))

#CASE - 5 : pure str into bool ---------POSSIBLE
a="SUDHA"
print(a,type(a))
b=bool(a)
print(b,type(b))





