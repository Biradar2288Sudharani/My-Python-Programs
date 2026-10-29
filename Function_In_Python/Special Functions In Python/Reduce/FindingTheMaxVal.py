# FindingTheMaxVal.py
# WAPP which will accept list of values and find maximum or heighest value, by using reduce function.
import functools
print("Enter values for list:")
lst1=[int(val) for val in input().split()]
maxval=functools.reduce(lambda a,b:a if a>b else b,lst1)
print("Maximum value({})={}".format(lst1,maxval))

''' --> ANSWER <--

'''

