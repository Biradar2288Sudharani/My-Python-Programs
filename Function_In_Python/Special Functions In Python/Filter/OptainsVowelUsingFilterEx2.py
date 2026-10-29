# OptainsVowelUsingFilterEx.py
# WAPP which will accept line of text and optain those words which are containing vowel words.
''' --> TASK <--
line : sky is blue and why not black
Excepted output : [is blue and not black]---vowel words
Excepted output : [sky,why]---consonant words
'''
# Logic 1
line=input("Enter line of Text:")
vowelwords=list(filter(lambda word:'a'  in word.lower() or 'e' in word.lower() or
                       'i' in word.lower() or 'o' in word.lower() or
                       'u' in word.lower(), line.split()))


consonantwords=list(filter(lambda word:'a' not in word.lower() and 'e' not in word.lower() and
                       'i' not in word.lower() and 'o' not in word.lower() and
                       'u' not in word.lower(), line.split()))
print("Given line of Text:{}".format(line))
print("Vowel Words={}".format(vowelwords))
print("Consonat Words={}".format(consonantwords))


# Logic 2
line=input("Enter line of Text:")
vowelwords=list(filter(lambda word:word.isalpha() and 'a'  in word.lower() or 'e' in word.lower() or
                       'i' in word.lower() or 'o' in word.lower() or
                       'u' in word.lower(), line.split()))


consonantwords=list(filter(lambda word:word.isalpha() and 'a' not in word.lower() and 'e' not in word.lower() and
                       'i' not in word.lower() and 'o' not in word.lower() and
                       'u' not in word.lower(), line.split()))
print("Given line of Text:{}".format(line))
print("Vowel Words={}".format(vowelwords))
print("Consonat Words={}".format(consonantwords))








