# validation of student number
while(True):
    sno=input("Enter student number:")
    if(sno.isdigit()):
        if(int(sno)>0):
            break
        else:
            print("\t {} Invalid Input for student number---Try Again!!!".format(sno))
    else:
        print("\t Student number should not be non-integer---Try Again!!!".format(sno))