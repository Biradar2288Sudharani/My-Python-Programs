#  iaAlnum Examples.py

# Example 1
a="apple"
print(a.isalnum()) # True

# Example 2
a="python 3.234"
print(a.isalnum()) # False

# Example 3
a="python314"
print(a.isalnum()) # True 

# Example 4
a="123_123"
print(a.isalnum()) #False

# Example 5
a="$123424"
print(a.isalnum()) #False

# Example 6
a="12345"
print(a.isalnum()) #True

# Example 7
a="!@#$%^&*"
print(a.isalnum()) #False