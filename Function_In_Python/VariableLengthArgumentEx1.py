# VariableLengthArgumentEx1.py
def disp(a,b,c,d,e):  # Function def-1
    print(a,b,c,d,e)
def disp(a,b,c,d):  # Function def-2
    print(a,b,c,d)
def disp(a,b,c):  # Function def-3
    print(a,b,c)
def disp(a,b):  # Function def-4
    print(a,b)
def disp(a):  # Function def-5
    print(a)
def disp():  # Function def-6
    print("Empty")
# Main Program
disp(10,20,30,40,50)  # Function Call-1 With 5 Arguments
disp(10,20,30,40)  # Function Call-2 With 4 Arguments
disp(10,20,30)  # Function Call-3 With 3 Arguments
disp(10,20)  # Function Call-4 With 2 Arguments
disp(10)  # Function Call-5 With 1 Arguments
disp()  # Function Call-6 With 0 Arguments
'''  --> ANSWER <--
TypeError: disp() takes 0 positional arguments but 5 were given
Because:
Above program not executr as it is because PVM remembers the
latest function defination due to it's interpretation time.
'''












