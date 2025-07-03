# isUpperExample.py
# Example 1
a="PYTHON"
print(a.isupper()) # True

# Example 2
a="python"
print(a.isupper()) # False

# Example 3
a="Python"
print(a.isupper()) # False

# Example 4
a="PYThon"
print(a.isupper()) # False

# Example 5
a="123"
print(a.isupper()) # False

# Example 6
a="!@#$%^&*()"
print(a.isupper()) # False

# Example 7
a="!@#$%^&*()123"
print(a.isupper()) # False

# Example 8
a="python12.3"
print(a.isupper()) # False