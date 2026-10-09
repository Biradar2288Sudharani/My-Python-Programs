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

# 6. Find Largest Number in a List ⭐⭐⭐⭐
numbers = [10, 25, 7, 45, 18]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
# OR - Without sorting
numbers = [10, 25, 5, 40, 15]
largest = float('-inf')
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)
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

# 9. Count Frequency of Characters ⭐⭐⭐⭐⭐
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
# OR
numbers = [1, 2, 2, 3, 4, 4, 5]
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)
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
'''
I iterate through every number in the list. I use the modulus operator to check the remainder when dividing by 2. If the remainder is zero, the number is even; otherwise, it is odd.”
'''

# 12. Sum of Digits ⭐⭐⭐
n = 12345
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n = n // 10
print(total)
'''
I initialize total to zero. The modulus operator extracts the last digit. I add that digit to total. Then integer division by 10 removes the last digit. I repeat this until the number becomes zero.”
'''

# 13. Reverse a Number ⭐⭐⭐
n = 1234
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)
'''
I extract the last digit using % 10. Then I shift the existing reverse number one position to the left by multiplying it by 10 and add the extracted digit. Finally, I remove the last digit from the original number using // 10.”
'''

# 14. Check Armstrong Number ⭐⭐⭐
n = 153
total = 0
temp = n
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10
if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")
'''
“I store the original number in n and make a temporary copy because I need the original number for comparison later. I extract each digit using % 10, cube the digit, and add it to total. After processing all digits, I compare the calculated total with the original number.”
'''

# 15. Find Common Elements Between Two Lists ⭐⭐⭐
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print(common)
'''
I create an empty list to store common elements. Then I iterate through the first list and check whether each element exists in the second list. If it exists, I append it to the result list.”
'''

# 16. Find Missing Number ⭐⭐⭐⭐ ⭐ - Suppose: [1, 2, 3, 5] Expected numbers are 1 to 5.
numbers = [1, 2, 3, 5]
n = 5
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
print(missing)
'''
I calculate the expected sum from 1 to n using the mathematical formula n * (n + 1) // 2. Then I calculate the actual sum of the list. The difference between these two sums gives me the missing number.”
'''

# 17. Check Anagram ⭐⭐⭐⭐ ⭐ - Two strings are anagrams if they contain the same characters with the same frequency.
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
'''
I sort both strings alphabetically. If both sorted strings are equal, they contain the same characters with the same frequency, so they are anagrams.”
'''

# 18. Find First Non-Repeating Character ⭐⭐⭐⭐ ⭐
text = "aabbcdde"

for char in text:
    if text.count(char) == 1:
        print(char)
        break
'''
I iterate through each character and use count() to find how many times that character occurs. If the count is exactly one, it is the first non-repeating character, so I print it and use break to stop the loop.”
'''

# 19. Sort a List Without sort() ⭐⭐⭐⭐
numbers = [5, 2, 8, 1, 3]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

'''
I compare each element with the elements after it. If the current element is greater than a later element, I swap them. By repeatedly doing this, smaller values move toward the beginning of the list.”
'''

# 20. Find Duplicate Elements ⭐⭐⭐⭐⭐
numbers = [1, 2, 3, 2, 4, 5, 3]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)
'''
I iterate through every number and check how many times it occurs using count(). If its frequency is greater than one, it is a duplicate. I also check num not in duplicates so that I don't add the same duplicate multiple times.”
'''


# 20. Find Duplicate Elements ⭐⭐⭐⭐
numbers = [1, 2, 3, 2, 4, 5, 3]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)
'''
I iterate through every number and check how many times it occurs using count(). If its frequency is greater than one, it is a duplicate. I also check num not in duplicates so that I don't add the same duplicate multiple times.”
'''

# 21. Count Frequency of Elements
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)

# 22. Count Characters in a String
text = "programming"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# 23. Reverse Words in a Sentence
sentence = "I love Python"
words = sentence.split()
reverse_words = words[::-1]
result = " ".join(reverse_words)
print(result)

# 24. Find Maximum Occurring Character
text = "programming"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
maximum = max(frequency, key=frequency.get)
print(maximum)

# 25. Flatten a Nested List - Input: numbers = [[1, 2], [3, 4], [5]] and Output: [1, 2, 3, 4, 5]
numbers = [[1, 2], [3, 4], [5]]
result = []
for sublist in numbers:
    for num in sublist:
        result.append(num)
print(result)

# 26. Sort List Without sort()
numbers = [5, 2, 8, 1, 3]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

# 27. Find Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)

# 28. Separate Positive and Negative Numbers
numbers = [-2, 5, -7, 8, 0, -1]
positive = []
negative = []
for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print(positive)
print(negative)

# 29. Find Common Characters
str1 = "python"
str2 = "programming"
common = set(str1) & set(str2)
print(common)

# 30. Find Length of String Without len()
text = "python"
count = 0
for char in text:
    count += 1
print(count)

# 31. Find the 
a=10
b=20
c=a*b
print(c)

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