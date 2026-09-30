# FilterDemoEx.py
def pos(n):
    if(n>0):
        return True
    else:
        return False
# Main Program
lst=[10,-20,-30,40,0,-60,50]
obj=filter(pos,lst)  # Filter concept --- here obj is an object of type <class,'filter'>
# Type Cast filter class object into list/tuple/set.
pslist=list(obj)
print("Given elements={}".format(lst))
print("Positive elements={}".format(pslist))








