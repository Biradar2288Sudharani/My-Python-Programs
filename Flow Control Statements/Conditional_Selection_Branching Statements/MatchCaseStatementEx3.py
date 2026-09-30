# MatchCaseStatementEx3.py
# Prigram for demonstrating Days in week 
# Logic 1
'''
Day's In Week:
1. Monday
2. Tuesday
3. Wednsday 
4. Thursday
5. Friday
6. Saturday
7. Sunday
-------------------------------
'''
print("\t Temperature Conversion Calculator:")
print("\t Monday")
print("\t Tuesday")
print("\t 3. Wednsday")
print("\t 4. Thursday")
print("\t 5. Friday")
print("\t 6. Saturday")
print("\t 7. Exit")
ch=input(" Enter Your Choice:")
match(ch):
    case "Monday":
        print("{} is Working Day".format(ch))
    case "Tuesday":
        print("{} is Working Day".format(ch))
    case "Wednesday":
        print("{} is Working Day".format(ch))
    case "Thursday":
        print("{} is Working Day".format(ch))
    case "Friday":
        print("{} is Working Day".format(ch))
    case "Saturday":
        print("{} is Week-End-Preparing Under Ground Action Plan".format(ch))
    case "Sunday":
        print("{} is Holy Day. Enjoy Your Day Students!!!".format(ch))
    case _:
        print("{} is Not Week Day".format(ch))

'''
# Logic 2
wkn=input("Enter Week Name:")
match(wkn.upper()):
match(wkn[0:3],upper()):
match(wkn.upper[0:3]):
    case "monday"|"tuesday"|"wednsday"|"thursday"|"friday":
        print("{} is Working Day".format(wkn))
    case "saturday":
        print("{} is Week-End-Preparing Under Ground Action Plan".format(wkn))
    case "sunday":
        print("{} is Holy Day".format(wkn))
    case _:
        print("{} is Not Week Day".format(ch))


# logic 3
wkn=input("Enter Week Name:")
if wkn.lower() in["mon","tue","wed","thurs","fri","sat","sun","monday","tuesday","wednsday","thursday","friday","saturday","sunday"]:
    match(wkn[0:3].upper()):
        case "mon"|"tue"|"wed"|"thurs"|"fri":
             print("{} is Working Day".format(wkn))
        case "sat":
            print("{} is Week-End-Preparing Under Ground Action Plan".format(wkn))
        case "sunday":
            print("{} is Holy Day".format(wkn))
        case _:
            print("{} is Not Week Day".format(ch))
'''

























