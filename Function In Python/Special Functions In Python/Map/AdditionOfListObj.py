# AdditionOfListObj.py
# WAPP which will compute addition of two list objects.
# Logic 1
print("Enter equal number of values for first list:")
lst1=[int(val) for val in input().split()]
print("Enter equal number of values for second list:")
lst2=[int(val) for val in input().split()]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("*"*50)
print("First List:{}".format(lst1))
print("*"*10)
print("First List:{}".format(lst1))
print("*"*10)
print("Sum List:{}".format(lst3))
print("*"*50)

# Logic 2
print("Enter equal number of values for first list:")
lst1=[int(val) for val in input().split()]
print("Enter equal number of values for second list:")
lst2=[int(val) for val in input().split()]
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst1)-len(lst2)):
        lst1.append(0)
# Now add the elements of lst1 and lst2
lst3=list(map(lambda a,b:a+b,lst1,lst2))
print("*"*50)
print("First List:{}".format(lst1))
print("*"*10)
print("First List:{}".format(lst1))
print("*"*10)
print("Sum List:{}".format(lst3))
print("*"*50)


''' --> ANSWER <--
Enter equal number of values for first list:
34 22 65 33
Enter equal number of values for second list:
23 55 78 43
**************************************************
First List:[34, 22, 65, 33]
**********
First List:[34, 22, 65, 33]
**********
Sum List:[57, 77, 143, 76]
**************************************************
'''