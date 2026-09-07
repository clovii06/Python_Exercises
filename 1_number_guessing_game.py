# 1. Number Guessing Game
"""
Pseudocode:
function guessing_game():
    answer = random number
    while True:
        get guess
        if guess < answer:
            display higher
        else if guess > answer:
            display lower
        else:
            display correct
            break
"""
import random

def guessing_game():
        answer = random.randint(1, 100)

        while True:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess < answer:
                print("Higher!")

            elif guess > answer:
                print("Lower!")

            else:
                print(f"You got it! The answer was {answer}.")
                break
