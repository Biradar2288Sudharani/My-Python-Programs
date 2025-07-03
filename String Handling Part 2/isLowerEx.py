# isLower Examples.py

# Example 1
a="PYTHON"
print(a.islower()) # False

# Example 2
a="python"
print(a.islower()) # True

# Example 3
a="Python"
print(a.islower()) # False

# Example 4
a="PYThon"
print(a.islower()) # False

# Example 5
a="123"
print(a.islower()) # False

# Example 6
a="!@#$%^&*()"
print(a.islower()) # False

# Example 7
a="!@#$%^&*()123"
print(a.islower()) # False

# Example 8
a="python12.3"
print(a.islower()) # True