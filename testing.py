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

    play()   


def play():
    """
    Prints the word length in underscores to the user.
    Sets the hangman to stage 6 / begining stage.
    """
    word = random.choice(word_list)
    print(word)
    word_guess = "_" * len(word)
    print(word_guess)
    stage = 6
    print(hangman(stage))
    # Set letters guessed as empty list that can have users guesses appended
    letters_guessed = []
    # Input box for answer
    user_input = input("Type a letter here:\n")
    # Function to check answer is valid
    check_answer(user_input)
    # If valid but wrong append to letters_guessed []


def check_answer(user_input):
   if len(user_input) == 1 and user_input.isalpha():
      print("yes")
   else:
      print(f"{user_input} is not a valid guess, please enter one letter.")


def hangman(stage):
    """
    Defines each stage of the hangman as items on a list which
    can be iterated as neccissary and displayed to the user.
    """
    stages = [  # Stage 0: head, body, arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   --_
                """,
                # Stage 1: head, body, arms, and leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   --_
                """,
                # Stage 2: head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   --_
                """,
                # Stage 3: head, body, and arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   --_
                """,
                # Stage 4: head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   --_
                """,
                # Stage 5: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   --_
                """,
                # Stage 6: base/empty template
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
