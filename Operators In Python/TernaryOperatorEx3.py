# WAPP program which will any word & decide whether it palindrom or not.
# TernaryOperatorEx3.py
# Logic 1
word=input(" Enter a word:")
reverse="palindrom" if word==word[::-1] else "not palindrom"
print("Word {} is {}".format(word,reverse))

# Logic 2
word=input(" Enter a word:")
reverse="palindrom" if word.lower()==word[::-1] else "not palindrom"
print("Word {} is {}".format(word,reverse))


















