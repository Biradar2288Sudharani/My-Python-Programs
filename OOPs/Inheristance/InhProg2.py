# InhProg2.py
class parent:
    def getparentprop(self):
        self.pp=float(input("Enter Parent Property:"))

class child(parent):
    def getchildprop(self):
        self.cp=float(input("Enter Child Property:"))

    def computetotprop(self):
        self.totprop=self.pp+self.cp

    def dispprop(self):
        print("*"*40)
        print("\t Property Details")
        print("*"*40)
        print("\t Parent Property:{}".format(self.pp))
        print("\t Child Property:{}".format(self.cp))
        print("\t Total Property:{}".format(self.totprop))
        print("*"*40)
        
# Main Program
c=child()
c.getparentprop()
c.getchildprop()
c.computetotprop()
c.dispprop()



