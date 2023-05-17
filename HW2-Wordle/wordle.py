# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Timothy Phan and Ibrahim Dobashi
# Date: 2/13/2023
# ----------------------------------------------------------------------
"""


and a more detailed description here.
"""

import random
import string

# Constant assignments
RED = '\033[91m'  # to print text in red: print(RED + text)
GREEN = '\033[92m'  # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)


def choose_wordle(filename):
    """
    Read the file specified and choose a random 5-letter word.
    :param filename: (string) name of the file to choose the wordle from
    :return: (string) the mystery word in uppercase
    """
    with open(filename, 'r', encoding='UTF-8') as input_file:
        file_output = input_file.read()

        word_list = [(word.strip(string.punctuation)) for word in
                     file_output.split()]

        five_letter_words = [word for word in word_list if len(word) == 5 and
                             word.isalpha()]
        return random.choice(five_letter_words).upper()


def check(wordle, guess):
    """
    Check the player's guess against the wordle and return a string
    representing the color coded feedback for the specified guess.
    Red indicates that the guessed letter is NOT in the word.
    Yellow indicates that the letter is in the word but not in the
    correct spot.
    Green indicates that the letter is in the word in the correct spot.
    :param wordle: (string) the mystery word in upper case
    :param guess: (string) the user's guess in upper case
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string

    working_list = list(wordle)  # creates a working list based off the wordle
    output = [''] * 5  # creates an output list to return the user guess
    for i in range(len(guess)):  #
        if guess[i] == working_list[i]:
            output[i] = GREEN + guess[i]
            working_list[i] = ''  # maps the index where a Green was found
    word = [w for w in working_list if w != '']  # removes the green letters
    for i in range(len(guess)):
        if guess[i] in word and not output[i]:
            output[i] = YELLOW + guess[i]
            word.remove(guess[i])
        elif not output[i]:
            output[i] = RED + guess[i]

    return ''.join(output)


def feedback(attempt):
    """
    Print the feedback corresponding to the number of attempts
    it took to guess the wordle.
    :param attempt: (integer) number of attempts needed to guess
    :return: None
    """
    match attempt:
        case 1:
            print(DEFAULT + "Genius!")
        case 2:
            print(DEFAULT + "Magnificent!")
        case 3:
            print(DEFAULT + "Impressive!")
        case 4:
            print(DEFAULT + "Splendid!")
        case 5:
            print(DEFAULT + "Great!")
        case 6:
            print(DEFAULT + "Phew!")


def prompt_guess():
    """
    Prompt the user repeatedly for a valid 5 letter guess that contains
    only letters.  Guess may be in lower or upper case.
    :return: (string) the user's valid guess in upper case
    """
    user_guess = input(DEFAULT + "Please enter your 5 letter guess: ")
    # checks if there are no numbers using isalpha and
    # that the user is inputting a 5-letter word
    while not (user_guess.isalpha() and len(user_guess) == 5):
        user_guess = input("Please enter your 5 letter guess: ")

    return user_guess.upper()


def play(wordle):
    """
    Implement the wordle game with all 6 attempts.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # enter your code below and take out the pass statement
    # call the prompt_guess function to prompt the user for each attempt
    # call the check function to build the colored feedback string
    # call the feedback function to print the final feedback if the user
    # guesses within 6 attempts

    # gives the user 6 tries of guessing the word through a for loop,
    # if the user doesn't guess in the 6th try,
    # it outputs the wordle
    for attempt in range(1, 7):
        print(DEFAULT + "Attempt", attempt)
        curr_guess = prompt_guess()
        check_guess = check(wordle, curr_guess)
        print(check_guess)
        if curr_guess == wordle:
            feedback(attempt)
            break

    if curr_guess != wordle:
        print(DEFAULT + "The correct answer is", wordle)


def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1. prompt the player for a filename
    # 2. call choose_wordle and get a random mystery word in uppercase
    #    from the file specified
    # 3. call play to give the user 6 tries
    # 4. if the user has not guessed the wordle, print the correct
    #    answer

    filename = input(
        "Please enter the filename: ")  # prompts the user for a filename

    mystery_word = choose_wordle(filename)
    play(mystery_word)


if __name__ == '__main__':
    main()
