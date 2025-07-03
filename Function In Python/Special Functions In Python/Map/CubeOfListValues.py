# CubeOfListValues.py
# WAPP which will accept list of numerical values and find quare of positive numbers and cubes of negative numbers.

print("Enter values for list:")
lst=[int(val) for val in input().split()]
print("Given List Of values:{}".format(lst))
poslst=list(filter(lambda value:value>0,lst))
neglst=list(filter(lambda value:value<0,lst))
possqrlst=list(map(lambda value:value**2,poslst))
negcubelst=list(map(lambda value:value**3,neglst))
print("Square List={}".format(possqrlst))
print("Cube List={}".format(negcubelst))

''' --> ANSWER <--

'''

