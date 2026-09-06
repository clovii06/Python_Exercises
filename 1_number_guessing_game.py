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

print("This is a number guessing game.")
guessing_game()

def guessing_game():
    number = random.randint(1, 30)
    guess = int(input("Guess the number between 1 and 30: "))