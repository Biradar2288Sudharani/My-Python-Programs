# WAPP which will accept list of values and find max and min elements by using functions (don't use max min functions).
# MaxMinEx.py
def readvalues():
     lst=()
     print("Enter list of values and press @ to stop:")
   
def findmax(lst):
    maxv=lst[0]
    for val in lst:
        if (maxv<val):
            maxv=val
        else:
            return maxv

def findmin(lst):
    minv=lst[0]
    for val in lst:
        if (minv>val):
            minv=val
        else:
            return minv
        
# Main Program
lst=readvalues()
if(len(lst)==0):
    print("List is empty---can't find max and min!!")
elif(len(lst)==1):
    print("Max and Min is same={}".format(lst[0]))
elif((len(set(lst))==1)):
    print("All values are equal and max and min is same={}".format(lst[0]))
else:
    maxv=findmax(lst)
    minv=findmin(lst)
    print("Max({})={}".format(lst,maxv))
    print("Min({})={}".format(lst,minv))










