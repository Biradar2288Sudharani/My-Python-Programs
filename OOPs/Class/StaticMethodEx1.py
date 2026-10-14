# StaticMethodEx1.py
# Program for demonstrating static method.
class student:
    def getstudvalues(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.smarks=float(input("Enter Student Marks:"))

class employee:
    def getempvalues(self):
        self.eno=int(input("Enter Employee Number:"))
        self.ename=input("Enter Employee Name:")

class teacher:
    def getteachervalues(self):
        self.tno=int(input("Enter Teacher Number:"))
        self.tname=input("Enter Teacher Name:")
        self.tsub=input("Enter Teacher Subject:")
        self.texp=int(input("Enter Teacher Experience:"))

class hyd:
    @staticmethod
    def dispobjectdata(objdata,objinfo):
        print("*"*50)
        print("'{}' Information".format(objinfo))
        print("*"*50)
        for dmn,dmv in objdata.__dict__.items():
            print("\t {} --> {}".format(dmn,dmv))
        print("*"*50)

# Main Program
s=student()
e=employee()
t=teacher()
s.getstudvalues()
e.getempvalues()
t.getteachervalues()

# Want to display any type of object content --- we need a method --- universal operation --- static method.
hyd.dispobjectdata(s,"student")  # static method accessed w.r.t class name.
hyd.dispobjectdata(e,"employee")  # static method accessed w.r.t class name.
hyd.dispobjectdata(t,"teacher")  # static method accessed w.r.t class name.








