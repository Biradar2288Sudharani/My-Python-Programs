# WAPP which will accept the age of citizen and whether citizen is eligible to vote or not.
# VoteEx.py
# Logic 1
age=int(input("Enter age of citizen:"))
if(age>=18):
    print("{} years citizens are eligible for vote".format(age))
else:
    print("{} years citizens are not eligible for vote".format(age))

# Logic 2
while(True):
    age=int(input("Enter age of citizen:"))
    if(age>=18):
        print("\t {} years citizens are eligible for vote".format(age))
        break
    else:
        print("\t {} years citizens are not eligible for vote".format(age))

# Logic 3
while(True):
    age=int(input("Enter age of citizen:"))
    if(age>=18)and(age<=100):
        print("\t {} years citizens are eligible for vote".format(age))
        break
    else:
        print("\t {} years citizens are not eligible for vote".format(age))














