# WAPP which will eliminate the duplicate value from list of values by using funvtions, don't convert list into set.
# EliminateDuplicateVal.py
# Logic 1
def readvalues():
    lst=[]
    print("Enter list of values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(value)
        else:
            break
    return lst

def uniquevalues(lst):
    if(len(lst)==0):
        print("List is empty --- Nothing to do.")
    else:
        s1=set()
        for val in lst:
            s1.add(val)
        else:
            print("List Of Value:{}".format(lst))
            print("Set Of Unique Values:{}".format(s1))

# Main Program
lst=readvalues()
uniquevalues(lst)

# Logic 2
def readvalues():
    lst=[]
    print("Enter list of values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(value)
        else:
            break
    return lst

def uniquevalues(lst):
    lst=readvalues()
    if(len(lst)==0):
        print("List is empty --- Nothing to do any operation.")
    else:
        s1=set()
        for val in lst:
            s1.add(val)
        else:
            print("List Of Value:{}".format(lst))
            print("Set Of Unique Values:{}".format(s1))

# Main Program
uniquevalues(lst)
 
# Logic 3
def readvalues():
    lst=[]
    print("Enter list of values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(value)
        else:
            break
    return lst

def uniquevalues(lst):
    lst=readvalues()
    if(len(lst)==0):
        print("List is empty --- Nothing to do any operation.")
    else:
        d1={}
        for val in lst:
            if val not in d1:
                d1[val]=1
            else:
                d1[val]=d1[val]+1
        else:
            print("List Of Value:{}".format(lst))
            s1=list(d1.keys())
            print("Set Of Unique Values:{}".format(s1))

# Main Program
uniquevalues(lst)


