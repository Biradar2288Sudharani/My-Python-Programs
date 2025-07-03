# KeywordArgumentEx1.py
'''
---> Concept Of Keyword Argument <---
My requrirement is 
A B C D
1 2 3 4
'''
def disp(a,b,c,d):
    print(a,b,c,d)
# Main Program
disp(1,2,3,4)  # Function  with positional arguments
disp(4,2,3,1)  # This line executed but give the wrong mapping and that mapping not same to my requirement.hence we can use keyword argument
disp(d=4,a=1,c=3,b=2) # Function call with ---> keyword argument
disp(1,d=4,c=3,b=2) # Function call with ---> Positional and keyword argument
# disp(d=4,2,3,a=1) ===> SyntaxError: positional argument follows keyword argument
# To solving above problem we can use keyword argument to all values.
disp(d=4,b=2,c=3,a=1) # Function call with ---> Positionak and keyword argument








