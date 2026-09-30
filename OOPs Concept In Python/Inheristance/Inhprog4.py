# Inhprog4.py

class grandparent:
    def getgrandparentprop(self):
        self.gp=float(input("Enter Grand Parent Property:"))

class parent:
    def getparentprop(self):
        self.pp=float(input("Enter Parent Property:"))

class child(grandparent,parent):
    def getchildprop(self):
        self.cp=float(input("Enter Child Property:"))

    def computetotprop(self):
        self.totprop=self.gp+self.pp+self.cp

    def dispprop(self):
        self.getgrandparentprop()
        self.getparentprop()
        self.getchildprop()
        self.computetotprop()
        print("*"*40)
        print("\t Property Details")
        print("*"*40)
        print("\t Grand Parent Property:{}".format(self.gp))
        print("\t Parent Property:{}".format(self.pp))
        print("\t Child Property:{}".format(self.cp))
        print("\t Total Property:{}".format(self.totprop))
        print("*"*40)
        
# Main Program
c=child()
c.dispprop()









