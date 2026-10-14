# InstanceMethodEx1.py
# Program for demonstrating instance method.
class student:
    def readstudvalues(self,objectinfo):
        self.sno=int(input("Enter {} Student Number:".format(objectinfo)))
        self.sname=input("Enter {} Student Name:".format(objectinfo))
        self.smarks=float(input("Enter {} Student Marks:".format(objectinfo)))

    def dispstuddata(self,objectinfo):
        print("{} Student Information".format(objectinfo))
        print("*"*50)
        print("Student Number {} ".format(self.sno))
        print("Student Name {} ".format(self.sname))
        print("Student Marks {} ".format(self.smarks))
        print("*"*50)

# Main Program
s1=student()  # Object Creation
s2=student()  # Object Creation
print("*"*50)
print("ID of s1={}".format(id(s1)))
print("ID of s2={}".format(id(s2)))
print("*"*50)

# Read the instance data for s1
s1.readstudvalues("First")  # Method Call
print("*"*50)

# Read the instance data for s2 
s2.readstudvalues("Second")  # Method Call

# Display s1 object data
s1.dispstuddata("First")  # Method Call

# Display s2 object data
s2.dispstuddata("Second")  # Method Call
