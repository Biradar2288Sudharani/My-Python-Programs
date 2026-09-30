# WAPP which will accept any digit & display the name of digit
# if-elif-elseStmtEx1.py
digit=int(input("Enter any digit:"))
if(digit==0):
    print("Given digit {} name is Zero".format(digit))
elif(digit==1):
    print("Given digit {} name is one".format(digit))
elif(digit==2):
    print("Given digit {} name is Two".format(digit))
elif(digit==3):
    print("Given digit {} name is Three".format(digit))
elif(digit==4):
    print("Given digit {} name is Zero".format(digit))
elif(digit==5):
    print("Given digit {} name is Five".format(digit))
elif(digit==6):
    print("Given digit {} name is Six".format(digit))
elif(digit==7):
    print("Given digit {} name is Seven".format(digit))
elif(digit==8):
    print("Given digit {} name is Eight".format(digit))
elif(digit==9):
    print("Given digit {} name is Nine".format(digit))
elif(digit not in[0,1,2,3,4,5,6,7,8,9] and digit>0):
    print("{} is Positive Number".format(digit))
elif(digit<0):
    print("{} is Negative Number".format(digit))














