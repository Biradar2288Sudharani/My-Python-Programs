# finding only max value
# OnlyMaxEx.py
def findmax(lst):
    maxv=lst[0]
    for val in lst:
        if (maxv<val):
            maxv=val
    else:
        return maxv
# Main Program
lst=[10,20,30,40,50]
maxv=findmax(lst)
print("Max Of This Set ({}) = {}".format(lst,maxv))