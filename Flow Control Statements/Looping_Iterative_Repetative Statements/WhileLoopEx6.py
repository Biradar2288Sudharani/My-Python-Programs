# WAPP which will accept any word or line of next & display each & every character, of a word or line of text.
# WhileLoopEx6.py
# Logic 1
line=input("Enter a word or line of text:")
i=0
while(i<=len(line)-1):
    print("\t\t{}".format([i]))
    i=i+1

# Logic 2
line=input("Enter a word or line of text:")
i=-len(line)
while(i<=-1):
    print("\t\t{}".format([i]))
    i=i+1

# Logic 3
import time
line=input("Enter a word or line of text:")
i=-len(line)
while(i<=-1):
    print("\t\t{}".format([i]))
    i=i+1
    time.sleep(2)
















