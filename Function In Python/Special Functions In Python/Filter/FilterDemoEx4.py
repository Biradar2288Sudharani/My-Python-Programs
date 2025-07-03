# FilterDemoEx4.py
print("Enter list of values seperated space:")
lst=[int(val) for val in input().split()]
posobj=tuple(filter(lambda n:n>0,lst))
negobj=tuple(filter(lambda n:n<0,lst))
print("Given elements={}".format(lst))
print("Positive elements={}".format(posobj))
print("Negative elements={}".format(negobj))









