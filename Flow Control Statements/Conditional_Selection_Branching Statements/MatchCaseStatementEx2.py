# MatchCaseStatementEx2.py
# WAPP which will implement following area of different figures:
'''
1. Rectangle
2. Square
3. Circle
4. Triangle
5. Exit
'''
print("\t Area of Diffrent Figures:")
print("\t 1. Rectangle")
print("\t 2. Square")
print("\t 3. Circle")
print("\t 4. Triangle")
print("\t 5. Exit")
ch=int(input(" Enter Your Choice:"))
match(ch):
    case 1:
        print("Area Of Rectangle")
        length,breadth=float(input("Enter Length:")),float(input("Enter Breadth:"))
        print("\t Area of Rectangle ({},{})={}".format(length,breadth,length*breadth))
    case 2:
        print("Area Of Square")
        side=float(input("Enter side:"))
        print("\t Area of Square ({})={}".format(side,side*side))
    case 3:
        print("Area Of Circle")
        radius=float(input("Enter Radius:"))
        print("\t Area of Square ({})={}".format(radius,3.14*radius**2))
    case 4:
        print("Area Of Triangle")
        height,breadth=float(input("Enter height:")),float(input("Enter breadth:"))
        print("\t Area of Triangle ({})={}".format(height,breadth,0.5*height*breadth))
    case 5:
        print("Thankas for using this program")
    case _:   # Default Case
        print("Your selection of is operation is wrong--Try Again!!!")
print("Program Execution Ended")














