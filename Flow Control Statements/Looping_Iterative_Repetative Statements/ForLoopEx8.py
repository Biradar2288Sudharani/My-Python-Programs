# WAPP which will accept a line of text and find number of words and their length in a given number of text.
# ForLoopEx8.py
# Logic 1
line=input("Enter any Line of Text:")
nows=line.split()
d=dict()
for word in nows:
    #print(word,"-->",nows)
    d[word]=len(word)
else:
    for word,length in d.items():
        print("\t{}-->{}".format(word,length))

# Logic 2
text=input("Enter a line of Text:")
print("Given Text:{}".format(text))
num_of_words=text.split()
print("Given Words={}".format(num_of_words))
print("Number Of Words={}".format(len(num_of_words)))





















