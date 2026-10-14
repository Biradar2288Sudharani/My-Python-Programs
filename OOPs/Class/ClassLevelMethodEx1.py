# ClassLevelMethodEx3.py
# Program for demonstrating class level methods.
class student:
    @classmethod
    def getcrs(cls):  # Class Level Method
        cls.crs="PYTHON"
        student.city="BANGLORE"
        # Here crs and city are called class level data members.
    
    def readstudvalues(self,objectinfo):  # Instance Method
        self.sno=int(input("Enter {} Student Number:".format(objectinfo)))
        self.sname=input("Enter {} Student Name:".format(objectinfo))
        self.smarks=float(input("Enter {} Student Marks:".format(objectinfo)))

    def dispstuddata(self,objectinfo):
        print("{} Student Information".format(objectinfo))
        print("*"*50)
        print("Student Number {} ".format(self.sno))
        print("Student Name {} ".format(self.sname))
        print("Student Marks {} ".format(self.smarks))
        print("Student Course {} ".format(self.crs))
        print("Student City {} ".format(self.city))
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

# call class level method w.r.t class name
student.getcrs()

# Display s1 object data
s1.dispstuddata("First")  # Method Call

# Display s2 object data
s2.dispstuddata("Second")  # Method Call






