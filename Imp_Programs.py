# 1. Reverse a String ⭐⭐⭐⭐⭐
text = "python"
reverse = text[::-1]
print(reverse)

# 2. Check Whether a String Is Palindrome ⭐⭐⭐⭐⭐
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
I first store the string. Then I reverse the string using slicing and compare it with the original string. 
If both are equal, it is a palindrome; otherwise it is not
'''

# 3. Find Factorial of a Number ⭐⭐⭐
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(factorial)
'''
I initialize factorial to 1 because multiplication should start from 1. Then the for loop runs from 1 to n. In every iteration, I multiply the current factorial value by i. For 5, 
the calculation becomes 1 × 2 × 3 × 4 × 5, which gives 120.”
'''

# 4. Fibonacci Series ⭐⭐⭐⭐
n = 7
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''
I initialize the first two Fibonacci numbers as 0 and 1. In every iteration, I print a. Then I simultaneously update a to b and b to a + b. 
Python's multiple assignment allows me to update both variables in one statement.”
'''