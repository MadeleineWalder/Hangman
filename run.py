# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list

# python3 run.py


def new_game():
    """
    Begins a new game by welcoming user
    and giving brief instrucions.
    """
    print("Welcome to Hangman!\n")
    print("Guess a letter by typing it and pressing the ENTER key.")
    print("Correct guesses will fill their place within the word.")
    print("Wrong guesses will result in the hangman being built.")
    print("Guess all correct letters of the word before he is complete!\n")

    get_random_word()


def get_random_word():
    """
    Assigns a random word from the word.py file to the variable 'word'.
    """
    word = random.choice(word_list)
    play(word)


def play(word):
    """
    Prints word_str to the user.
    """
    word_guess = "_" * len(word)
    print(word_guess)


def hangman(stage):
    """
    Defines each stage of the hangman as items on a list which
    can be iterated as neccissary and displayed to the user.
    """
    stages = [  # 6th stage: head, body, arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   --_
                """,
                # 5th stage: head, body, arms, and leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   --_
                """,
                # 4th stage: head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   --_
                """,
                # 3rd stage: head, body, and arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   --_
                """,
                # 2nd stage: head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   --_
                """,
                # 1st stage: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   --_
                """,
                # base/empty template
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   --_
                """
    ]
    return stages[stage]


new_game()
