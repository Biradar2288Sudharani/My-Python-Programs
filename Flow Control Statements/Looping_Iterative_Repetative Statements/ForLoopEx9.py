# WAPP which will accept line of text and find height word length , whose length is heighest.
# ForLoopEx9.py
line=input("Enter any Line of Text:")
nows=line.split()
d=dict()
for word in nows:
    d[word]=len(word)
else:
    # dv=d.values()
    # dv=list(d.values())
    dv=max(list(d.values()))
    print("dv")
    lst=list()  # Creating empty list for adding heighest length word.
    for k,v in d.items():
        if(v==dv):
            #print(k)
            lst.append(k)
    else:
        print("Heighest Length Word:")
        for val in lst:
            print("\t\t{}".format(val))

















