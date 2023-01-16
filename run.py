'''
Imports
'''
import os
import random
from words import WORD_LIST
from hangman import __HANGMAN_STAGES__, display_hangman

# python3 run.py


def clear_screen():
    '''
    Function which clears the terrminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def new_game():
    '''
    The start where the user is welcomed and given brief instrucions.
    '''
    print("\n")
    print("Welcome to Hangman!")
    print("Guess the letters in the word before the hangman is complete!\n")
    question()


def question():
    '''
    If user input is valid, runs game for "Y" (Yes) and ends game for "N" (No).
    '''
    play_question = take_user_input_for_play()
    if play_question == "Y":
        print("Great, lets play!\n")
        play_game()
    elif play_question == "N":
        print("Okay, click 'Run Program' above if you change your mind!")


def take_user_input_for_play():
    '''
    Asks user if they want to play.
    '''
    play_question = 'A'
    print("Would you like to play? (Y / N)\n")
    while play_question not in ['Y', 'N']:
        play_question = input().upper()
        if play_question not in ['Y', 'N']:
            print("Please answer 'Y' for yes or 'N' for no.")
    return play_question


def play_game():
    '''
    Selects a random word from words.py. Shows user word length in underscores.
    Takes the user input if valid and assigns it to letters_guessed list.
    If user input is in the word it will be added in correct place. If not a
    hangman stage is added. Checks if underscores are still present, if not
    user must have won as the word must be complete.
    '''
    word = random.choice(WORD_LIST)
    word_length = "_" * len(word)
    print("_ " * len(word))
    stage = 6
    display_hangman(stage)
    letters_guessed = []
    word_complete = False
    while not word_complete and stage > 0:
        user_input = ask_user_for_letter(letters_guessed, word)
        if user_input in word:
            print(f"Correct! {user_input} is in the word!\n")
            letters_guessed.append(user_input)
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
    '''
    Shows important information to the user at the begining of the game
    and after each guess is processed.

    :param word_length: The word in underscores which correct letters replace.
    :param letters_guessed: List of letters user has already guessed.
    :param stage: The stage of the hangman.
    '''
    print(" " + word_length)
    print("\n")
    print('Letters guessed:' + ' ' + ', '.join(letters_guessed))
    display_hangman(stage)


def display_final_result(word_complete, word):
    '''
    Congratulates user if word completed and they won the game.
    Or tells them if they ran out of guesses and what the correct answer was.

    :param word_complete: The win condition.
    :param word: The word that they needed to guess. The correct answer.
    '''
    if word_complete:
        print("Congratulations! You completed the word!\n")
    else:
        print(f"You ran out of guesses! The word was: {word}.\n")


def ask_user_for_letter(letters_guessed, word):
    '''
    Checks if user input is valid by checking it is one letter in the alphabet.
    If letter already guessed / invalid it tells them & asks for another input.

    :param letters_guessed: List of letters user has already guessed.
    :param word: The word containing the letters which the user must guess.
    :return: The user input if valid.
    '''
    user_input = ''
    user_input_invalid = True
    while user_input_invalid:
        user_input = input("Type a letter here:\n").lower()
        if user_input in letters_guessed:
            print(f"Oops, you already guessed {user_input}\n")
        elif len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Please enter one letter")


if __name__ == '__main__':
    clear_screen()
    new_game()
