# WAPP which will accept any value and find its reverse, without using slicing operation.
# ForLoopEx7.py
# Logic 1
'''
value=int(input("Enter Any Value:"))
for index in range(len(value)-1,-1,-1):
    print(value[index])
    rv=rv+value[index]
else:
    print("Reverse of ({})={}".format(value,rv))
'''

# WAPP which will accept any value and find its reverse, using slicing operation.
# Logic 2
value=input("Enter Any Value:")
reverse=value[::-1]
print(value,"-->",reverse)

# In this example concatination is using for reverse data.














