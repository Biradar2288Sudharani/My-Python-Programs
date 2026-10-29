# KeywordVariableLengthArguEx1.py
def disp(sno,sname,cm,cpp,cp):
    print(sno,sname,cm,cpp,cp)
def disp(eno,ename,hb1,hb2,hb3):
    print(eno,ename,hb1,hb2,hb3)
def disp(a,b,c,d):
    print(a,b,c,d)
def disp(tno,tname):
    print(tno,tname)
def disp(bno):
    print(bno)

# Main Program
disp(sno=10,sname="Sudha",cm=50,cpp=60,cp=70) # Function call-1 with 5 keyword variable length arguments.
disp(eno=100,ename="XYZ",hb1="Reading",hb2="Writing",hb3="Swimming") # Function call-2 with 5 keyword variable length arguments.
disp(a=10,b=20,c=30,d=40) # Function call-3 with 4 keyword variable length arguments.
disp(tno=1,tname="KVR") # Function call-4 with 2 keyword variable length arguments.
disp(bno="BOI2288") # Function call-5 with 1 keyword variable length arguments.

'''  --> ANSWER <--
TypeError: disp() got an unexpected keyword argument 'sno'
This program will not execute because
TypeError: disp() got an unexpected keyword argument 'sno'
PVM remembers latest function defination due to interpretation process
'''






