# VariableLengthArgumentEx3.py
def disp(*a):  # Here *a is called variable length parameter and whose type is tuple. 
    print(a,type(a),len(a))
# Main Program
disp(10,20,30,40,50)  # Function Call-1 With 5 Arguments
disp(10,20,30,40)  # Function Call-2 With 4 Arguments
disp(10,20,30)  # Function Call-3 With 3 Arguments
disp(10,20)  # Function Call-4 With 2 Arguments
disp(10)  # Function Call-5 With 1 Arguments
disp()  # Function Call-6 With 0 Arguments











