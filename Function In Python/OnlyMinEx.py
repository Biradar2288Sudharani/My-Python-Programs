# finding only min value
# OnlyMinEx.py
def findmin(lst):
    minv=lst[0]
    for val in lst:
        if (minv>val):
            minv=val
        else:
            return minv
# Main Program
lst=[10,20,30,40,50]
minv=findmin(lst)
print("Min Of This Set ({}) = {}".format(lst,minv))







