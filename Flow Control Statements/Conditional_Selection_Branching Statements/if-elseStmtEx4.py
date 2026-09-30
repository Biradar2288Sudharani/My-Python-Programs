# WAPP which will accept any digit & display the name of digit
# if-elseStmtEx4.py
digit=int(input("Enter any digit:"))
if(digit==0):
    print("Given digit {} name is Zero".format(digit))
else:
    if(digit==1):
        print("Given digit {} name is one".format(digit))
    else:
        if(digit==2):
            print("Given digit {} name is Two".format(digit))
        else:
            if(digit==3):
                print("Given digit {} name is Three".format(digit))
            else:
                if(digit==4):
                    print("Given digit {} name is FOur".format(digit))
                else:
                    if(digit==5):
                        print("Given digit {} name is Five".format(digit))
                    else:
                        if(digit==6):
                            print("Given digit {} name is Six".format(digit))
                        else:
                            if(digit==7):
                                print("Given digit {} name is Seven".format(digit))
                            else:
                                if(digit==8):
                                    print("Given digit {} name is Eight".format(digit))
                                else:
                                    if(digit==9):
                                        print("Given digit {} name is Nine".format(digit))
                                    else:
                                        if(digit not in[0,1,2,3,4,5,6,7,8,9] and digit>0):
                                            print("{} is Positive Number".format(digit))
                                        else:
                                            print("{} is Negative Number".format(digit))














