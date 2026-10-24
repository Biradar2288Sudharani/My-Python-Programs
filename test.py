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

'''
🔥 Tier A — Do first
#9 Character Frequency
#17 Anagram
#18 First Non-Repeating Character
#20 Duplicate Elements
#16 Missing Number
#2 Palindrome
#1 Reverse String
#7 Second Largest
#4 Fibonacci
#5 Prime
🟠 Tier B — Do next
#10 Remove Duplicates
#6 Largest Number
#19 Sort Without sort()
#24 Maximum Occurring Character
#23 Reverse Words
#15 Common Elements
#25 Flatten Nested List
#12 Sum of Digits
#13 Reverse Number
#14 Armstrong Number
🟡 Tier C — Good basics, lower priority
#3 Factorial
#8 Count Vowels
#11 Even/Odd
#21 Element Frequency
#22 Character Count — overlaps heavily with #9
#26 Sort Without sort() — duplicate of #19
#27 Even/Odd — duplicate of #11
#28 Positive/Negative
#29 Common Characters
#30 String Length Without len()
'''

print("Hello Sudha!")




















