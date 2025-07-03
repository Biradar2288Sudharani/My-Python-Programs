# PolymorphismEx11.py

class teacher:
    def advise(self):    # Original Method
        print("Teacher Advise is Read Python Notes in Two Daily!!!")
        print("Teacher Advise is Practice Python Program in One Daily!!!")

class sincierstudent(teacher):
    def advise(self):  # Overriden Method
        print("Senier student follows teacher advise!!!")
        print("Senier student always chat with friends!!!")
        super().advise()

class lazystudent(teacher):
    def advise(self):   # Overriden Method
        print("Lazy student follows teacher advise!!!")
        print("Lazy student always chat with friends!!!")
        super().advise()

# Main Program
ss=sincierstudent()
ss.advise()
print("*"*50)
ls=lazystudent()
ls.advise()
