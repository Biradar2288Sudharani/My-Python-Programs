# Special points about logical operators
# LogicalOperatorsSpecialPointsEx.py

# "and" Operator
print(100 and 200)
print(-100 and -234)
print(100 and 0)
print(0 and 120)
print(100 and True)
print(100 and False)
print(100 and 1.2)
print(100 and 200 and 300)
print(100 and 0 and 300)
print(0 and 0 and 300)

 """ "and" Operator Answers
200
-234
0
0
True
False
1.2
300
0
0
"""

# "or" Operator

print(100 or 200)
print(0 or 300)
print(100 or True)
print(0 or 0.5)
print(0 or 10 or 0)
print("True" or "False")
print("False" or "True")
print(0 or "python" or -123)


""" "or" Operator Answer
100
300
100
0.5
10
True
False
python
"""

# Combination of "and" And "or" Operator
print(10 and 20 or 30)
print(10 or 20 and -10 or 30)
print(100 and 200 and 300 or 400)
print(100 and 200 and 300 or 400 and not 100)
print(True and "False" or True or "hyd" and "python")
print("   " and " " or "")

""" Combination of "and" And "or" Operator Answer
20
10 
300
300
False
"""