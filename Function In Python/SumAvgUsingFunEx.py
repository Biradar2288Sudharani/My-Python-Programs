# WAPP which will accept list of values and find sum and average without using predefined function sum by using function concept.
# SumAvgUsingFunEx.py
# Logic 1
def readvalues():
    lst=[]
    print("Enter list of values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(float(value))
        else:
            break
    return lst

def findsum(lst):
    if(len(lst)==0):
        print("List is empty --- can't find sum")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum({})={}".format(lst,s))
            avg=findavg(s,len(lst))      # Function Call
            print("Avg({})={}".format(lst,avg))

def findavg(s,nov):
    avg=s/nov
    return avg

# Main Program
lst=readvalues()  # Function Call
findsum(lst)      # Function Call

# Logic 2
def readvalues():
    lst=[]
    print("Enter list of values and press @ to stop:")
    while(True):
        value=input()
        if(value!="@"):
            lst.append(float(value))
        else:
            break
    return lst

def findsum(lst):
    lst=readvalues()
    if(len(lst)==0):
        print("List is empty --- can't find sum")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum({})={}".format(lst,s))
            avg=findavg(s,len(lst))      # Function Call
            print("Avg({})={}".format(lst,avg))

def findavg(s,nov):
    avg=s/nov
    return avg

# Main Program
findsum(lst)      # Function Call


