# VariableLengthArgumentEx6.py
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
disp(100,"Sudha",10,20,30,40,50)
disp(200,"Sunil",10,20,30,40)
disp(300,"Sushil",10,20,30)
disp(400,"Suvedh",10,20)
disp(500,"Suhas",10)
disp(600,"Suman")


# OR
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
disp(10,20,30,40,50)  # Function Call-1 With 5 Arguments
disp(10,20,30,40)  # Function Call-2 With 4 Arguments
disp(10,20,30)  # Function Call-3 With 3 Arguments
disp(10,20)  # Function Call-4 With 2 Arguments
disp(10)  # Function Call-5 With 1 Arguments
disp()  # Function Call-6 With 0 Arguments







