# KeywordArgumentEx2.py
def disp(a,b,c,d):
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))
# Main Program
print("*"*50)
print("\tA\tB\tC\tD")
print("*"*50)
disp(10,20,30,40) # Function  with positional arguments
disp(d=40,b=20,a=10,c=30)  # Function call with ---> keyword argument
disp(10,d=40,b=20,c=30) # Function call with ---> Positional and keyword argument






