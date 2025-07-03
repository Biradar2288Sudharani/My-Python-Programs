# WAPP which accept any numerical value & decide whether it is even or odd
# TernaryOperatorEx6.py
num=int(input("Enter a number:"))
res="even" if num%2==0 else "odd" 
print("{} is {}".format(num,res))