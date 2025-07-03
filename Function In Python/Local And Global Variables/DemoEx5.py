# DemoEx5.py
def learnAI():
    sub1="AI"
    print("To develop '{}' applications, we use '{}' language".format(sub1,lang))

def learnML():
    sub2="ML"
    print("To develop '{}' applications, we use '{}' language".format(sub2,lang))

def learnDL():
    sub3="DL"
    print("To develop '{}' applications, we use '{}' language".format(sub3,lang))
# Main Program
learnAI()  # Here can't access lang value because it was defined after function call.
lang="PYTHON"  # Here lang is called global variable.
learnML()
learnDL()

'''  --> ANSWER <--
When we write main program as this format then error is generated i.e,
NameError: name 'lang' is not defined. Did you mean: 'range'?
'''








