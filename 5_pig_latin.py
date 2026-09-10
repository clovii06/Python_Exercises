# 5. Pig Latin
"""
Pseudocode:

function pig_latin():
    get english_word

    if english_word[0] in 'aeiou':
        pig_latin_word = english_word + "way"
else:
    slice first letter
    move first letter to end
    pig_latin_word = english_word + "ay"

display pig_latin_word

"""
def pig_latin():
    """Translate english word to pig latin"""
    english_word = input("Word: ")

    # If first letter is a vowel
    if english_word[0] in 'aeiou':
        pig_latin_word = english_word + "way"

    # If first letter is a consonant
    else:
        pig_latin_word = english_word[1:] + english_word[0] + "ay"

    print(pig_latin_word)

pig_latin()