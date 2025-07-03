# MatchCaseStatementEx4.py
# WAPP which will implement following:
'''
Temperature Conversion Calculator:
1. Fohrenheit to Celcius
2. Fohrenheit to Kelvin
3. Celcius to Fohrenheit 
4. Celcius to Kelvin
5. Kelvin to Celcius
6. Kelvin to Fohrenheit
7. Exit
-------------------------------
Enter Your Choice: 
---> FORMULAS <---
1. Fohrenheit to Celcius = c = (f-32)(5/9)
2. Fohrenheit to Kelvin  = k = (f-32)(5/9) + 273.15
3. Celcius to Fohrenheit = f = c(9/5) + 32
4. Celcius to Kelvin     = k = c + 273.15
5. Kelvin to Celcius     = c = k - 273.15
6. Kelvin to Fohrenheit  = f = (k - 273.15)(9/5) + 32
'''
print("\t Temperature Conversion Calculator:")
print("\t 1. Fohrenheit to Celcius")
print("\t 2. Fohrenheit to Kelvin")
print("\t 3. Celcius to Fohrenheit")
print("\t 4. Celcius to Kelvin")
print("\t 5. Kelvin to Celcius")
print("\t 6. Kelvin to Fohrenheit")
print("\t 7. Exit")
ch=int(input(" Enter Your Choice:"))
match(ch):
    case 1:
        print("Fohrenheit to Celcius Conversion")
        f=float(input("Enter Fahrenheit:"))
        c = f-32*5/9
        print("The Conversion of {} is in Celcius {}".format(f,c))
    
    case 2:
        print("Fohrenheit to Kelvin Conversion")
        f=float(input("Enter Fahrenheit:"))
        k = f-32*5/9 + 273.15
        print("The Conversion of {} is in Kelvin {} ".format(f,k))
    
    case 3:
        print("Celcius to Fohrenheit Conversion")
        c=float(input("Enter Celcius:"))
        f = c*9/5 + 32
        print("The Conversion of {} is in Fohrenheit {} ".format(c,f))
    
    case 4:
        print("Celcius to Kelvin Conversion")
        c=float(input("Enter Celcius:"))
        k = c + 273.15
        print("The Conversion of {} is in Kelvin {}".format(c,k))
    
    case 5:
        print("Kelvin to Celcius Conversion")
        k=float(input("Enter Kelvin:"))
        c = k - 273.15
        print("The Conversion of {} is in Celcius {} ".format(k,c))
    
    case 6:
        print("Kelvin to Fohrenheit Conversion")
        k=float(input("Enter Kelvin:"))
        f = (k - 273.15)(9/5) + 32
        print("The Conversion of {} is in Foherenheit {} ".format(k,f))
    
    case 7:
        print("Thankas for using this program")
    
    case _:   # Default Case
        print("Your selection of is operation is wrong--Try Again!!!")
print("Program Execution Ended")




















