# 5. Pig Latin
"""
Pseudocode:

get english_word

if english_word[0] = vowel:
    add "way"

else:
    slice first letter
    move first letter to end
    add "ay"

display pig_latin_word

"""

english_word = input("Word: ")
if english_word[0] in 'aeiou':
    print("This is a vowel")
else:
    print(english_word[1:len(english_word)]) # If consonant, remove first letter