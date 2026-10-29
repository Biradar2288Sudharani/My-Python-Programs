# FilterDemoEx2.py
def pos(n):
    if(n>0):
        return True
    else:
        return False
def neg(n):
    if(n<0):
        return True
    else:
        return False
# Main Program
print("Enter list of values seperated space:")
lst=[int(val) for val in input().split()]
posobj=tuple(filter(pos,lst))
negobj=tuple(filter(neg,lst))
print("Given elements={}".format(lst))
print("Positive elements={}".format(posobj))
print("Negative elements={}".format(negobj))
