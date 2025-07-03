# WAPP which will implement the following problem.
# ValidationEx.py
'''
=> Accept student number , name and marks in 3 subjects.
   c lang marks(cm) ,   c++ marks(cppm) ,   python marks(pm)
       (100)                (100)               (100)

=> Calculate total marks(total marks=cm+cppm+pm) and 
   percentage of marks(percent=(total marks/300)*100)

=> Decide the result--Fail:
   condition for fail: Student scored less than 40 in any of the subject.

=> Decide the result--Pass:
   (a) Distinction  (b) First  (c) Second  (d) Third

   (a) Student passed in distinction provided total marks 
       ranges between 300 and 250 (inclusive)
   (b) Student passed in First provided total marks 
       ranges between 249 and 200 (inclusive)
   (c) Student passed in Second provided total marks 
       ranges between 199 and 150 (inclusive)
   (d) Student passed in Third provided total marks 
       ranges between 149 and 100 (inclusive)

=> Display student marks reports:
'''
# Logic 1
#     ---> PROGRAM <---
# validation of student number
while(True):
    sno=input("Enter student number:")
    if(sno.isdigit()):
        if(int(sno)>0):
            break
        else:
            print("\t {} Invalid Input for student number---Try Again!!!")
    else:
        print("\t Student number should not be non-integer---Try Again!!!")
print("*"*5)

# validation of student name
while(True):
    sname=input("Enter student name:")
    if(sname.isalpha()):  # name is pure alphabet not alpha numeric
        break
    else:
        print("\t {} Invalid Input for student name---Try Again!!!".format(sname))
print("*"*5)

# validation of C lang Marks
while(True):
    clm=input("Enter student C lang Marks:")
    if(clm.isdigit()):
        cm=int(clm)
        if(cm>=0) and (cm<=100):
            break
        else:
            print("\t {} Invalid C lang marks---Try Again!!".format(cm))
    else:
        print("\t {} Invalid input for C lang marks---Try Again!!".format(clm))
print("*"*5)

# validation of CPP lang Marks
while(True):
    cpplm=input("Enter student CPP lang Marks:")
    if(cpplm.isdigit()):
        cppm=int(cpplm)
        if(cppm>=0) and (cppm<=100):
            break
        else:
            print("\t {} Invalid CPP lang marks---Try Again!!".format(cppm))
    else:
        print("\t {} Invalid input for CPP lang marks---Try Again!!".format(cpplm))
print("*"*5)

# validation of PYTHON lang Marks
while(True):
    pylm=input("Enter student PYTHON lang Marks:")
    if(pylm.isdigit()):
        pym=int(pylm)
        if(pym>=0) and (pym<=100):
            break
        else:
            print("\t {} Invalid PYTHOM|N lang marks---Try Again!!".format(pym))
    else:
        print("\t Invalid input for PYTHON lang marks---Try Again!!".format(pylm))
print("*"*5)

# Calculate Total Marks:
totmarks = cm+cppm+pym
percent = round((totmarks/300)*100,2)
if(cm<40) or (cppm<40) or (pym<40):
    grade = "Fail"
else:
    if(250<=totmarks<=300):
        grade = "Distinction"
    elif(200<=totmarks<=249):
        grade = "First"
    elif(150<=totmarks<=199):
        grade = "Second"
    elif(100<=totmarks<=149):
        grade = "Third"
print("*"*5)

# Display Student Marks:
print("\t\t Student Marks Report:")
print("\t\t\t\t Student Number:{}".format(sno))
print("\t\t\t\t Student Name:{}".format(sname))
print("\t\t\t\t Student C Lang Mark:{}".format(cm))
print("\t\t\t\t Student CPP Lang Mark:{}".format(cppm))
print("\t\t\t\t Student PYTHON Lang Mark:{}".format(pym))
print("\t\t\t\t Student Totak Marks:{}".format(totmarks))
print("\t\t\t\t Student Percentage Of Marks:{}".format(percent))
print("\t\t\t\t Student Result:{}".format(grade))
print("*"*50)

# Logic 2
# validation of student number
while(True):
    sno=input("Enter student number:")
    if(sno.isdigit()):
        if(int(sno)>0):
            break
        else:
            print("\t {} Invalid Input for student number---Try Again!!!")
    else:
        print("\t Student number should not be non-integer---Try Again!!!")
print("*"*5)

# validation of student name
while(True):
    sname=input("Enter student name:")
    words=sname.split()
    res=True
    for word in words:
        if(not word.isalpha()):
            res=False
            break
    if(res):
        print("{} Is valid name:".format(sname))
        break
    else:
        print("{} Is not valid student name:".format(sname))
print("*"*5)

# validation of C lang Marks
while(True):
    clm=input("Enter student C lang Marks:")
    if(clm.isdigit()):
        cm=int(clm)
        if(0<=cm>=100):
            break
        else:
            print("\t {} Invalid C lang marks---Try Again!!".format(cm))
    else:
        print("\t {} Invalid input for C lang marks---Try Again!!".format(clm))
print("*"*5)

# validation of CPP lang Marks
while(True):
    cpplm=input("Enter student CPP lang Marks:")
    if(cpplm.isdigit()):
        cppm=int(cpplm)
        if(0<=cppm>=100):
            break
        else:
            print("\t {} Invalid CPP lang marks---Try Again!!".format(cppm))
    else:
        print("\t {} Invalid input for CPP lang marks---Try Again!!".format(cpplm))
print("*"*5)

# validation of PYTHON lang Marks
while(True):
    pylm=input("Enter student PYTHON lang Marks:")
    if(pylm.isdigit()):
        pym=int(pylm)
        if(0<=pym>=100):
            break
        else:
            print("\t {} Invalid PYTHOM|N lang marks---Try Again!!".format(pym))
    else:
        print("\t Invalid input for PYTHON lang marks---Try Again!!".format(pylm))
print("*"*5)

# Calculate Total Marks:
totmarks = cm+cppm+pym
percent = round((totmarks/300)*100,2)
if(cm<40) or (cppm<40) or (pym<40):
    grade = "Fail"
else:
    if(250<=totmarks<=300):
        grade = "Distinction"
    elif(200<=totmarks<=249):
        grade = "First"
    elif(150<=totmarks<=199):
        grade = "Second"
    elif(100<=totmarks<=149):
        grade = "Third"
print("*"*5)

# Display Student Marks:
print("\t\t Student Marks Report:")
print("\t\t\t\t Student Number:{}".format(sno))
print("\t\t\t\t Student Name:{}".format(sname))
print("\t\t\t\t Student C Lang Mark:{}".format(cm))
print("\t\t\t\t Student CPP Lang Mark:{}".format(cppm))
print("\t\t\t\t Student PYTHON Lang Mark:{}".format(pym))
print("\t\t\t\t Student Totak Marks:{}".format(totmarks))
print("\t\t\t\t Student Percentage Of Marks:{}".format(percent))
print("\t\t\t\t Student Result:{}".format(grade))