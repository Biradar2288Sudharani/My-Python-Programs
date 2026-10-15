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

# 5. Check Prime Number ⭐⭐⭐⭐
n = 17
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
'''
A prime number is greater than 1 and has only two factors: 1 and itself. So I first check whether the number is less than or equal to 1. 
Then I check whether any number from 2 to n-1 divides it completely. If n % i is zero, it has another factor and is not prime. 
If the loop completes without finding a divisor, it is prime.”
'''