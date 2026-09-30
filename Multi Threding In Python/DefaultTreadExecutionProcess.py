# Program for demonstrating how main thread executes the functions in program---default execution program
# DefaultTreadExecutionProcess.py
import threading
def hello():
    print("*"*50)
    print("Line 4-> Executed By:",threading.current_thread().name)
    print("*"*50)

def hi():
    print("*"*50)
    print("Line 9-> Executed By:",threading.current_thread().name)
    print("*"*50)

def welcome():
    print("*"*50)
    print("Line 14-> Executed By:",threading.current_thread().name)
    print("*"*50)
# main program
print("*"*50)
print("Main Program Executed By:",threading.current_thread().name)
print("*"*50)
hello() #Function Call 1
hi() # Function Call 2
welcome() # Function Call 3
print("*"*50)
print("Line->26 Main Program Execution Ended")
print("*"*50)