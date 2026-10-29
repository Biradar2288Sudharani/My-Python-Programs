# Max&MinValueEx.py
# WAPP which will accept list of values and find the max and min by using anonymous function.
# Logic 1
values=list(map(int, input("Enter a list of numbers separated by space: ").split()))
findmax=lambda values:max(values)
# Main Program
res=findmax(values)
print("Max Value=",res)
print("*"*50)
findmin=lambda values:min(values)
# Main Program
res=findmin(values)
print("Min Value=",res)
print("*"*50)

# Logic 2
maxvalue=lambda a,b,c,d:max(a,b,c,d)
# Main Program
a,b,c,d=int(input("Enter value of a:")),int(input("Enter value of b:")),int(input("Enter value of c:")),int(input("Enter value of d:"))
res=maxvalue(a,b,c,d)
print("Max Value({},{},{},{})={}".format(a,b,c,d,res))
print("*"*50)
minvalue=lambda a,b,c,d:min(a,b,c,d)
# Main Program
a,b,c,d=int(input("Enter value of a:")),int(input("Enter value of b:")),int(input("Enter value of c:")),int(input("Enter value of d:"))
res=minvalue(a,b,c,d)
print("Min Value({},{},{},{})={}".format(a,b,c,d,res))
print("*"*50)

# Logic 3
# Accept list of values
values = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# Find the maximum and minimum using lambda functions
max_value = lambda x: max(x)
min_value = lambda x: min(x)

# Print the results
print("Maximum value:", max_value(values))
print("Minimum value:", min_value(values))
