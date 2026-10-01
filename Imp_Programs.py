# 1. Reverse a String ⭐⭐⭐
text = "python"
reverse = text[::-1]
print(reverse)

# 2. Check Whether a String Is Palindrome ⭐⭐⭐
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

# 4. Fibonacci Series ⭐⭐⭐
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

# 5. Check Prime Number ⭐⭐⭐
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

# 6. Find Largest Number in a List ⭐⭐⭐
numbers = [10, 25, 7, 45, 18]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
'''
I initially assume the first element is the largest. Then I iterate through every element. 
If the current number is greater than largest, I update largest. After the loop finishes, it contains the maximum value.”
'''

# 7. Find Second Largest Number ⭐⭐⭐
numbers = [10, 25, 7, 45, 18]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(unique_numbers[-2])
'''
“First, I convert the list into a set to remove duplicate values. Then I convert it back into a list and sort it in ascending order. 
The last element is the largest and the second-last element is the second largest.”
'''

# 8. Count Vowels in a String ⭐⭐⭐
text = "python programming"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)
'''
I create a string containing all vowels and initialize the counter to zero. Then I iterate through every character. 
If the character exists in the vowels string, I increment the counter. Finally, I print the total number of vowels.”
'''

# 9. Count Frequency of Characters ⭐⭐⭐
text = "banana"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
'''
I use a dictionary because dictionaries store data as key-value pairs. Each character becomes a key and its occurrence count becomes the value. 
If the character already exists, I increase its count; otherwise, I initialize it to 1.”
'''

# 10. Remove Duplicates from a List ⭐⭐⭐
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
'''
A set automatically stores only unique elements. So I convert the list into a set to remove duplicates and then convert it back into a list.”
'''

# 11. Find Even and Odd Numbers ⭐⭐⭐
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd")

























