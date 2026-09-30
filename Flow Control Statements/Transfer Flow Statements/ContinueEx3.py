# Program for reading values
# ContinueEx3.py
lst=list()
print("Enter values to stop @ inputting:")
while(True):
    value=input()
    if(value!="@"):
        lst.append(value)
    else:
        break
print("List of values:{}".format(lst))

# --> OR <--
lst=list()
print("Enter values to stop @ inputting:")
while(True):
    value=input("Enter value choice and press @ to stop:")
    if(value!="@"):
        lst.append(value)
    else:
        break
print("List of values:{}".format(lst))


































