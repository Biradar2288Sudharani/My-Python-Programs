# VariableLengthArgumentEx7.py
'''
def disp(sno,sname,*a,scity="HYD"):
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student City:{}".format(scity))
    s=0
    for val in a:
        print("{}".format(val),end=" ")
        s=s+val
        print()
    else:
        print("Sum={}".format(s))
        print("*"*20)
# Main Program
disp(100,"Sudha",10,20,30,40,50,"USA")
disp(200,"Sunil",10,20,30,40)
disp(300,"Sushil",10,20,30)
disp(400,"Suvedh",10,20)
disp(500,"Suhas",10)
disp(600,"Suman")
# ANSWER : TypeError: unsupported operand type(s) for +: 'int' and 'str'

Resolving Above Problem By
'''
def disp(sno,sname,*a,scity="HYD"):
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student City:{}".format(scity))
    s=0
    for val in a:
        print("{}".format(val),end=" ")
        s=s+val
        print()
    else:
        print("Sum={}".format(s))
        print("*"*20)
# Main Program
disp(100,"Sudha",10,20,30,40,50,scity="USA")
disp(200,"Sunil",10,20,30,40)
disp(300,"Sushil",10,20,30)
disp(400,"Suvedh",10,20)
disp(500,"Suhas",10)
disp(600,"Suman")