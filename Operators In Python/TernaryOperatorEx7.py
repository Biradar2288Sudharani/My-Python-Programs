# # WAPP which accept any numerical value & decide whether it is positive or negative
# TernaryOperatorEx7.py
num=int(input("Enter a number:"))
res="positive" if num>=0 else "negative" 
print("{} is {}".format(num,res))
