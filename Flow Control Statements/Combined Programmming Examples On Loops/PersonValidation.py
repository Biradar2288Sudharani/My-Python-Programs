# WAPP which will validate the name of the person or place or thing.
# PersonValidation.py
while(True):
    line=input("Enter any name / product / place:")
    print("Given Name:",line)
    words=line.split()
    res=True
    for word in words:
        if(not word.isalpha()):
            res=False
            break
    if(res):
        print("{} Is valid name:".format(line))
    else:
        print("{} Is not valid name:".format(line))













