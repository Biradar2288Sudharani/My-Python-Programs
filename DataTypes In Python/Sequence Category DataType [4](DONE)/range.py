# SYNTAX 1: varname=range(value)
a=range(10)
print(a,type(a))
for i in a:
    print(i)
for i in range(10):
    print(i)
for i in range(6):
    print(i)
for i in range(6):
    print(i,end="")

# SYNTAX 2: varname=range(start,stop)
a=range(10,16)
print(a,type(a))
for i in a:
    print(i)
for i in range(100,120):
    print(i)
    
# SYNTAX 3: varname=range(start,stop,step)
a=range(10,21,2)
print(a,type(a))
for val in a:
    print(val)
for val in range(20,9,-2):
    print(val)

# EXAMPLES FOR CODING
# Q.1) 0 1 2 3 4 5 6 7 8 9
for val in range(0,10):
    print(val)
for val in range (10):
    print(val)
    
# Q.2) 10 11 12 13 14 15 16 17 18 19 20
for i in range(10,21):
    print(i)
for i in range(10,21,1):
    print(i)

# Q.3) 100 101 102 103 104 105
for i in range(100,106):
    print(i)
for i in range(100,106,1):
    print(i)
    
# Q.4) -10 -11 -12 -13 -14 -15
for i in range (-10,-16):
    print(i)
for i in range (-10,-16,-1):
    print(i)


# Q.5) 10 9 8 7 6 5 4 3 2 1
for i in range (10,0):
    print(i)
for i in range (10,0,-1):
    print(i)


# Q.6) -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
for i in range (-10,0):
    print(i)
for i in range (-10,0,1):
    print(i)

# Q.7) -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
for i in range (10,0):
    print(i)
for i in range (-1,-11,-1):
    print(i)

# Q.8) 10 12 14 16 18
for i in range (10,21,2):
    print(i)
for i in range (10,0,2):
    print(i)

# Q.9)  100 110 120 130 140 150
for i in range (100,151,10):
    print(i)

# Q.10) -20 -18 -16 -14 -12 -10
for i in range (-20,-9,-2):
    print(i)

# Q.11) -1000 -900 -700 -600 -500
for i in range (-1000,-499,100):
    print(i)

# Q.12) -5 -4 -3 -2 -1 0 1 2 3 4 5
for i in range (-5,6,-1):
    print(i)
for i in range (-10,0,1):
    print(i)
