# TemperatureConversion.py
from TemperatureMenu import menu
menu()
from CF import ctof
from CK import ctok
from KC import ktoc
from KF import ktof
from FC import ftoc
from FK import ftok
import sys
while(True):
    ch=int(input("Enter Your Choice:"))
    match(ch):
        case 1:
            ctof()
        case 2:
            ctok()
        case 3:
            ktoc()
        case 4:
            ktof()
        case 5:
            ftoc()
        case 6:
            ftok()
        case 7:
            print("Thanks For Using This Program")
            sys.exit()
        case _:
            print("Your selection ofchoice is wrong --- Try Again!!!")
            













