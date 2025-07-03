# WAPP which will accept any word and decide whether it is a vowel word or not , without using membership operator and by using anonymous function.
# ConsonantOrVowelEx.py
convow=lambda word:"vowel" if word=='a' and word=='e' and word=='i' and word=='o' and word=='u' else " word is consnent"
# Main Program
word=input("Enter a word:")
res=convow(word)
print("Given word {}  {}".format(word,res))



# Accept a word from the user
word = input("Enter a word: ")
# Anonymous function to check if the first letter is a vowel (without membership operator)
is_vowel_word = lambda w:(w == 'a' or w == 'e' or w == 'i' or w == 'o' or w =='u') 
result = "Vowel word" if is_vowel_word(word) else "Is consonant word"
print(result)
#res=convow(word)
#print("Given word {}  {}".format(word,res))

