# WAPP which will accept list of word and get single line of text. by using reduce function.
# GettingSingleLineText.py
import functools
print("Enter list of words:")
lst=[str(val) for val in input().split()]
print("Given list of words={}".format(lst))
line=functools.reduce(lambda word1,word2:word1+""+word2,lst)
print("Line:{}".format(line))

''' --> ANSWER <--

'''