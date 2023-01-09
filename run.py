"""
Import random and my words from words.py file to use in game
"""
import random
from words import word_list

# python3 run.py


def new_game():
    """
    The start where the user is welcomed and given brief instrucions.
    """
    print("\n")
    print("Welcome to Hangman!\n")
    print("Guess a letter by typing it and pressing the ENTER key.")
    print("Correct guesses will fill their place within the word.")
    print("Wrong guesses will result in a stage of the hangman being added.")
    print("Guess all correct letters of the word before he is complete!\n")

    question()


def question():
    """
    Asks user if they want to play when the program is run and after each game.
    """
    play_question = input("Would you like to play? (Y/N)\n").upper()
    if play_question == "Y":
        print("Great, lets play!\n")
        play_game()
    else:
        print("Okay, we hope you change your mind!")
        new_game()


def play_game():
    """
    Picks & prints random word in underscores. Sets hangman to begining
    stage. Creates list for guessed letters. Sets win condition to False. 
    Takes user input and processes accordingly until user wins or looses.
    """
    word = random.choice(word_list)
    word_length = "_" * len(word)
    print(word_length)
    stage = 6
    print(hangman(stage))
    letters_guessed = []
    word_complete = False
    # Check answer is valid
    while not word_complete and stage > 0:
        user_input = input("Type a letter here:\n").lower()
        if len(user_input) == 1 and user_input.isalpha():
            # For correct answers:
            if user_input in word:
                print(f"Correct! {user_input} is in the word!\n")
                # Code by 'Kite'. More info in readme.md under 'Credit'.
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
                letters_guessed.append(user_input)
                stage -= 1
        else:
            print(f"'{user_input}' Not a valid guess, please enter one letter.\n")
        # Print important information for user to see
        print(word_length)
        print("\n")
        print(', '.join(letters_guessed))
        print(hangman(stage))
    if word_complete:
        print("Congratulations! You completed the word!\n")
    else:
        print("Unlucky! You ran out of guesses.")
        print(f"The word was: {word}.\n")

    question()


def hangman(stage):
    """
    Defines each stage of the hangman
    """
    stages = [  # Stage 0: head, body, arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     L L
                   |
                """,
                # Stage 1: head, body, arms, and leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |       L 
                   |
                """,
                # Stage 2: head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   |
                """,
                # Stage 3: head, body, and arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   |
                """,
                # Stage 4: head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   |
                """,
                # Stage 5: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   |
                """,
                # Stage 6: begining
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   |
                """
    ]
    return stages[stage]


new_game()
