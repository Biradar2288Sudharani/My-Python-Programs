# SumOfListUsingReduce.py
# WAPP which will accept list of values and find their sum by using reduce function.
# Logic 1
import functools
print("Enter values for list:")
lst1=[int(val) for val in input().split()]
res=functools.reduce(lambda x,y:x+y,lst1)
print("Sum({})={}".format(lst1,res))

# Logic 2
import functools
def sumop(a,b):
    return a+b
# Main Program
print("Enter value for list:")
lst1=[int(val) for val in input().split()]
res=functools.reduce(sumop,lst1)
print("Sum({})={}".format(lst1,res))




