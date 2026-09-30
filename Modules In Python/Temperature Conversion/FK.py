# FK.py---File Name and Module Name
def ftok():
    f=float(input("Enter temperature in terms of fahrenheit(F):"))
    k=(f-32)*(5/9)+273.15
    print("Kelvin Temperature:{}".format(k))