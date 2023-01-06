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

    play_game()


def play_game():
    """
    Picks a random word from words.py & prints length in underscores.
    Sets the hangman to stage 6 (begining). Takes user input.
    """
    word = random.choice(word_list)
    word_length = "_" * len(word)
    print(word_length)
    stage = 6
    print(hangman(stage))
    # Set empty list that can have users guesses appended
    letters_guessed = []
    # Set variable for win condition
    word_complete = False
    # Check answer is valid
    while not word_complete and stage > 0:
        user_input = input("Type a letter here:\n")
        if len(user_input) == 1 and user_input.isalpha():
            # For correct answers:
            if user_input in word:
                print(f"Correct! {user_input} is in the word!\n")
                # Code used here is from a Python YouTube tutorial by
                # the channel 'Kite'. Line 32-38 from their code.
                word_as_list = list(word_length)
                indices = [
                    i for i, letter in enumerate(word) if letter == user_input
                    ]
                for index in indices:
                    word_as_list[index] = user_input
                word_length = "".join(word_as_list)
                if "_" not in word_length:
                    word_complete = True
                # Code from Kite ends here
            # For already guessed answers:
            elif user_input in letters_guessed:
                print(f"Oops, you already guessed {user_input}\n")
            # For wrong answers:
            else:
                print("Letter not in word\n")
                # Add to letters guessed
                letters_guessed.append(user_input)
                # Add a stage to hangman
                stage -= 1
        else:
            print(f"{user_input} is not a valid guess, please enter one letter.\n")
        print(word_length)
        print("\n")
        print(', '.join(letters_guessed))
        print(hangman(stage))
    if word_complete:
        print("Congratulations! You completed the word!\n")
    else:
        print("Unlucky! You ran out of guesses.\n")


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
