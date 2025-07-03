# MatchCaseStatementEx1.py
# WAPP which will implement the following menu drivan application
'''Arithmetic Operations
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulo Division
6. Exponentiation
7. Exit
-----------------------
Enter Your Choice:
'''
print("\t Arithmetic Operations:")
print("\t 1. Addition:")
print("\t 2. Subtraction")
print("\t 3. Multiplication")
print("\t 4. Division")
print("\t 5. Modulo Division")
print("\t 6. Exponentiation")
print("\t 7. Exit")
ch=int(input(" Enter Your Choice:"))
match(ch):
    case 1:
        print("Enter two values for Addition:")
        a,b=float(input()),float(input())    
        print("\t Sum ({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter two values for Subtraction:")
        a,b=float(input()),float(input())    
        print("\t Subtraction ({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter two values for Multiplication:")
        a,b=float(input()),float(input())    
        print("\t Multiplication ({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter two values for Division:")
        a,b=float(input()),float(input())    
        print("\t Division ({},{})={}".format(a,b,a/b))
        print("\t Floor Division ({},{})={}".format(a,b,a//b))
    case 5:
        print("Enter two values for Module Dividsion:")
        a,b=float(input()),float(input())    
        print("\t Module Dividsion ({},{})={}".format(a,b,a%b))
    case 6:
        print("Enter two values for Exponentiation:")
        a,b=float(input("Enter Base:")),float(input("Enter Base:"))    
        print("\t Exponentiation ({},{})={}".format(a,b,a^b))
    case 7:
        print("Thankas for using this program")
    case _:   # Default Case
        print("Your selection of is operation is wrong--Try Again!!!")
print("Program Execution Ended")
















