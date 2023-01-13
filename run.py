""" Import random and my words from words.py file to use in game"""
import random
from words import WORD_LIST

from hangman import __HANGMAN_STAGES__, display_hangman

# python3 run.py


def new_game():
    """
    The start where the user is welcomed and given brief instrucions.
    """
    print("\n")
    print("Welcome to Hangman!")
    print("Guess the letters in the word before the hangman is complete!\n")

    question()


def question():
    """
    Asks user if they want to play when the program is run and after each game.
    """
    play_question = take_user_input_for_play()
    if play_question == "Y":
            print("Great, lets play!\n")
            play_game()
    elif play_question == "N":
        print("Okay, we hope you change your mind!")
        
def take_user_input_for_play():
    play_question = 'A';
    print("Would you like to play? (Y/N)\n")
    while play_question not in ['Y', 'N']:
        play_question = input().upper()
        if play_question not in ['Y', 'N']:
            print("Please answer 'Y' for yes or 'N' for no.")
    return play_question


def  play_game():
    word = random.choice(WORD_LIST)
    word_length = "_" * len(word)
    print(word_length)
    stage = 6
    print(display_hangman(stage))
    letters_guessed = []
    word_complete = False
    # Check answer is valid
    while not word_complete and stage > 0:
        user_input = ask_user_for_letter(letters_guessed, word)
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
        else:
            print("Letter not in word\n")
            letters_guessed.append(user_input)
            stage -= 1
        user_guess_result(word_length, letters_guessed, stage)
    display_final_result(word_complete, word)
    question()        

            
def user_guess_result(word_length, letters_guessed, stage):
    print(word_length)
    print("\n")
    print(', '.join(letters_guessed))
    display_hangman(stage)


def display_final_result(word_complete, word):
    if word_complete:
        print("Congratulations! You completed the word!\n")
    else:
        print(f"You ran out of guesses! The word was: {word}.\n")


def ask_user_for_letter(letters_guessed, word):
    user_input = 'asdfas'
    user_input_invalid = True
    while user_input_invalid:
        user_input = input("Type a letter here:\n").lower()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        elif (user_input in letters_guessed):
            print(f"Oops, you already guessed {user_input}\n")    
        else:
            print('please enter a letter')


if __name__ == '__main__':
    new_game()
