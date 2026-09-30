# StudentDetailsEx.py
# WAPP which will accept student details and write to the file.
# Read the data fromkeyboard.
sno=input("Enter Student Number:")
sname=input("Enter Student Name:")
smarks=input("Enter Student Marks:")
# Write the student data to the file
with open("student.data","a+") as fp:
    fp.write(sno+"\t")
    fp.write(sname+"\t")
    fp.write(smarks+"\n")
    print("Student data saved into file.")
    print("*"*50)
with open("student.data","a+") as fp:
    while(True):
        sno=input("Enter Student Number:")
        sname=input("Enter Student Name:")
        smarks=input("Enter Student Marks:")
        # Write the student to the file
        fp.write(sno+"\t")
        fp.write(sname+"\t")
        fp.write(smarks+"\n")
        print("Student data saved into file.")
        print("*"*50)
        ch=input("Do you want to insert one record(YES/NO):")
        if(ch.lower()=="NO"):
            print("Thanks For Using This Program")
            break
            









