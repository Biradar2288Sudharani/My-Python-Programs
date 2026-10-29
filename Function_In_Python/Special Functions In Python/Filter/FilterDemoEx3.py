# FilterDemoEx3.py
pos=lambda n:n>0   # Anonymous Function
neg=lambda n:n<0   # Anonymous Function
# Main Program
print("Enter list of values seperated space:")
lst=[int(val) for val in input().split()]
posobj=tuple(filter(pos,lst))
negobj=tuple(filter(neg,lst))
print("Given elements={}".format(lst))
print("Positive elements={}".format(posobj))
print("Negative elements={}".format(negobj))








