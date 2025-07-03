# WAPP which will implement the following.
# ContinueEx6.py
''' --> This Is Case Study One <--
Given Line Of Text : string47126 or string47py1th20n6
Expected Output : [string python]
Expected Output : [47126]...[426]...[17]
              AND
    --> This Is Case Study Two <--
Given Line Of Text : string47126 or string47py1th20n6
Expected Output : [642]...Decending Order(Even Number)
Expected Output : [17]...Asending Order(Odd Number)
'''
strlist=list()
numlist=()
line=input("Enter a line of Text:")
for ch in line:
    if(ch.isalpha()):
        strlist.append(ch)
    elif(ch.isdigit()):
        numlist.append(int(ch))
    else:
        strline=""
        strline=strline.join(strlist)
        print("String Data={}".format(strline))
        ed,od=[],list()
        for d in numlist:
            if(d%2==0):
                ed.append(d)
            else:
                od.append(d)
        print("Even List={}".format(ed))
        print("Odd List={}".format(od))
        ed.sort(reverse=True)
        print("Sorted Even List={}".format(ed))
        od.sort(reverse=False)
        print("Sorted Odd List={}".format(od))
        rstrdata=""
        rstrdata=rstrdata.join(sorted(strline))
        print("Reverse Data={}".format(rstrdata))


















