# OptainsVowelUsingFilterEx.py
line=input("Enter a line of text:")
vowlist=list(filter(lambda word:'a' in word.lower() or
                    'e' in word.lower() or'i' in word.lower() or
                    'o' in word.lower() or 'u' in word.lower() ,line))
print("Given Line={}".format(line))
print("Vowels List={}".format(vowlist))

print("------------OR-----------")

line=input("Enter a line of text:").lower()
vowlist=list(filter(lambda word:'a' in word or
                    'e' in word or'i' in word or
                    'o' in word or 'u' in word ,line))
print("Given Line={}".format(line))
print("Vowels List={}".format(vowlist))

''' --> ANSWER <--
Enter a line of text:he is not my brother he is my heart beat.
Given Line=he is not my brother he is my heart beat.
Vowels List=['e', 'i', 'o', 'o', 'e', 'e', 'i', 'e', 'a', 'e', 'a']
------------OR-----------
Enter a line of text:my brother is my breath.
Given Line=my brother is my breath.
Vowels List=['o', 'e', 'i', 'e', 'a']
'''









