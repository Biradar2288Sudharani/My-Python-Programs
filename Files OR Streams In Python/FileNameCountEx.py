# FileNameCountEx.py
# WAPP which will find number of lines , number of words and number of characters in a file.

# Logic 1
try:
    srcfile=input("Enter Source File Name:")
    with open(srcfile,"r") as fp:
        lines=fp.readlines()
        print("Number Of Lines={}".format(len(lines)))
except FileNotFoundError:
    print("Source File Doesn't Exist.")         

# Logic 2
try:
    srcfile=input("Enter Source File Name:")
    n1=0
    with open(srcfile,"r") as fp:
        lines=fp.readlines()
        for line in lines:
            n1=n1+1
        else:
            print("Number Of Lines={}".format(n1))
except FileNotFoundError:
    print("Source File Doesn't Exist.")

# Logic 3
try:
    srcfile=input("Enter Source File Name:")
    n1,nw,nc=0,0,0
    with open(srcfile,"r") as fp:
        lines=fp.readlines()
        for line in lines:
            n1=n1+1
            nw=nw+len(line.split())
            nc=nc+len(line)
        else:
            print("Number Of Lines={}".format(n1))
            print("Number Of Words={}".format(nw))
            print("Number Of Charcters={}".format(nc))
except FileNotFoundError:
    print("Source File Doesn't Exist.")



















