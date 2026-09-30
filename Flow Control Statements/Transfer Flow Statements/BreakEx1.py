# Demo Example using for loop
# my requirement is to display "sudha" without using indexing and slicing
# BreakEx1.py
s="sudharani"
for val in s:
    if(val=="r"):
        break
    else:
        print("\t\t{}".format(val))
else:
    print("I am from else part of for loop!")


# --> OR <--
s=input("Enter a Word:")
for val in s:
    if(val=="h"):
        break
    else:
        print("\t\t{}".format(val))
else:
    print("I am from else part of for loop!")




























