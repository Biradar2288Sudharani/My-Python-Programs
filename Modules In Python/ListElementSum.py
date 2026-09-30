# ListElementSum.py----File name and Module Name
''' IMP QUESTION
Excepted Input : [123,567,2189,17,8,45,345]
Excepted Otuput: [6,18,20,8,8,9,12]
'''
def listdigitssum():
    print("Enter list of values seperated by space:")
    lst=[int(val) for val in input().split()]
    sumlist=[]
    for val in lst:
        sval=str(val)
        s=0
        for digit in sval:
            s=s+int(digit)
        else:
            sumlist.append(s)
    else:
        print("Given Input List:{}".format(lst))
        print("Sum List:{}".format(sumlist))

''' --> ANSWER <--
Enter list of values seperated by space:
123 567 2189 17 8 45 345  
Given Input List:[123, 567, 2189, 17, 8, 45, 345]
Sum List:[6, 18, 20, 8, 8, 9, 12]
'''









