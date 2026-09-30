# DemoEx4.py
def learnAI():
    sub1="AI"    
    print("To develop '{}' applications, we use '{}' language".format(sub1,lang))
    # print(sub2,sub3) here sub2 & sub3 are local variables in another function definations.
def learnML():
    sub2="ML"
    print("To develop '{}' applications, we use '{}' language".format(sub2,lang))
    # print(sub1,sub3) here sub1 & sub3 are local variables in another function definations.
    
def learnDL():
    sub3="DL"
    print("To develop '{}' applications, we use '{}' language".format(sub3,lang))
    # print(sub1,sub2) here sub1 & sub2 are local variables in another function definations.

# Main Program
lang="PYTHON"  # Here lang is called global variable.
learnAI()
learnML()
learnDL()










