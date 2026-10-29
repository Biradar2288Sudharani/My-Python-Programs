# WAPP which will find number of word in a given lone of text by using anonymous function.
# CountWordEx.py
countwords=lambda word: len(word.split())  # Anonymous Function
# Main Program 
word=input("Enter a word or line of text:")
wordcount=countwords(word)  # Anonymous Function Call
print("Given Word or Line:{}".format(word))
print("Number of char={}".format(wordcount))














