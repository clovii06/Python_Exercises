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
def pig_latin():
    english_word = input("Word: ")

    if english_word[0] in 'aeiou':
        pig_latin_word = english_word + "way"
    else:
        pig_latin_word = english_word[1:len(english_word)] + english_word[0] + "ay"

    print(pig_latin_word)

pig_latin()