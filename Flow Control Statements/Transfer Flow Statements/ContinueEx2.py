# WAPP which will acccept list of numerical values and find list of positive numbers and negative numbers.
# ContinueEx2.py
'''
Given List=[10,-30,15,14,-5,6,-13,-40]
Expected Output=Positive List:[10,15,14,6]
Expected Output=Negative List:[-30,-5,-13,-40]
'''
n=int(input("Enter how many values you have:"))
if(n<=0):
    print("{} Is Invalid Input".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List Of Values:{}".format(lst))
        # coding for obtaining list of positive values
        pvlist=[]
        for val in lst:
            if (val<=0):
                continue
            pvlist.append(val)
        else:
            # coding for obtaining list of negative values
            nvlist=[]
        for val in lst:
            if (val>=0):
                continue
            nvlist.append(val)
        else:
            print("List Of Positive Values:{}".format(pvlist))
            print("List Of Negative Values:{}".format(nvlist))


















