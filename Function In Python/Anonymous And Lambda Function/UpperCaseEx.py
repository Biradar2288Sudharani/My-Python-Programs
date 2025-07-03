# UpperCaseEx.py
# WAPP which csn accept any word and converts into upper case.

convertcase=lambda word : word.upper()  # Anonymous Function

# Main Function
word=input("Enter a word or line of text:")
upperword=convertcase(word)  # Anonymous Function Call
print("Given Word or Line: {}".format(word))
print("Upper Case Word or Line: {}".format(upperword))





