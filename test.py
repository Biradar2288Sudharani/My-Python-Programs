a='sudha'
b=len(a)
print(b

# 📘 Q1. WAPP to Sum All the Items in a List
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total = total + i
print("Sum = ", total)   

# 📘 Q2. WAPP to Multiply All the Items in a List
numbers = [1, 2, 3, 4, 5]
total = 1
for i in numbers:
    total = total * i
print("Multifly = ", total)

# 📘 Q3. WAPP to Get the Largest Number from a List
numbers = [34, 24, 56, 22, 53, 32]

# Using for loop logic
largest  = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest Number = ", largest)

# Using max() function
largest = max(numbers)
print("Largest Number = ", largest)

# 📘 Q4. WAPP to Get the Smallest Number from a List
numbers = [34, 24, 56, 22, 53, 32]

# Using for loop logic
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest Number = ", smallest)

# Using min() function
smallest = min(numbers)
print("Smallest Number = ", smallest)

# 📘 Q5. WAPP to Count the Number of Strings Where String Length is 2 or More and the First & Last Characters are the Same. Sample List
words = ['abc', 'xyz', 'aba', '1221', '233', '12541', '11', '2']
count = 0
matched_words = []
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1
        matched_words.append(word)
print("Count of Word = ", count)
print("Matched Words = ", matched_words))

# 🔥 30. Find Numbers Appearing More Than Once
numbers = [1, 2, 3, 2, 4, 3, 5, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():
    if count > 1:
        print(num, count)