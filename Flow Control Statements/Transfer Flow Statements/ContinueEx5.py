
# WAPP which will accept list of names and sort them in both assending and decending orders.
# ContinueEx5.py
lst=list()
n=int(input("Enter list of names and press @ to stop inputting:"))
while(True):
    val=input()
    if(val!="@"):
        lst.append(val)
    else:
        break
print("List of values:{}".format(lst))
# sort of data in asending order
lst.sort()
print("Assending Order:{}".format(lst))
lst.sort(reverse=True)
print("Decending Order:{}".format(lst))





































