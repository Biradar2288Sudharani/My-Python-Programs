# Split or Delimeter Examples.py

# Example 1
a="Python is oop Language"
print(len(a)) # 22
print(a.split()) # ['Python', 'is', 'oop', 'Language']
print(len(a.split())) # 4

# Example 2
a="Python is oop Language"
print(len(a)) # 22
print(a.split()) # ['Python', 'is', 'oop', 'Language']
print(len(a.split())) # 4
b=a.split()
print(type(b)) # <class 'list'>

'''
# Example 3
a="22-06-2003"
b=a.split()
print(b) #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
'''
# Example 3
a="22-6-2003"
b=a.split("-")
print(b) # ['22-6-2003']
print("Day=",b[0]) # Day= 22
print("Month=",b[1]) # Month= 6
print("Year=",b[2]) # Year= 2003








