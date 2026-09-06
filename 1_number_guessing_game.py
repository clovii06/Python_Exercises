# 1. Number Guessing Game

"""
Pseudocode:
display welcome
guessing_game()

function guessing_game():
    number = random number
    get guess
    if guess > number:
        display lower
        get guess
    else if guess < number:
        display higher
        get guess
    else:
        display correct
"""
import random

print("I'm thinking of a number between 1 and 30. Guess!")
guessing_game()

def guessing_game():
    number = random.randint(1, 30)