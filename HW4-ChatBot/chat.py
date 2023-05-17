# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s):Timothy Phan & Ibrahim Dobashi
# Date: 2/27/2023
# ----------------------------------------------------------------------
"""
This is a simple chatbot program that talks with the user

In this program, the user is prompted to enter their name and what they
want to say to the chatbot. There are a total of 12 cases that the
program chooses from based on the user's responses. There are 2
functions called chat_with and change_person. The chat_with contains
the 12 cases the program will choose based on the user's responses. The
change_person function is used only in cases 3 and 7 where the pronouns
in the user's response gets changed and returns a string with the
changed pronouns and the rest of the words
"""
import random
import string


# Enter your constant assignments below
# Enter the function definition & docstring for the change_person
# function below
# Enter function definitions & docstrings for any other helper functions
def chat_with(name):
    """
    Takes user's name and responds to the user's input
    :param name: string
    :return: Boolean
    """
    SPECIAL_TOPICS = {'family', 'friend', 'friends', "mom", 'dad',
                      'brother', 'sister',
                      'girlfriend', 'boyfriend', 'children', 'son', 'daughter',
                      'child', 'wife', 'husband', 'home', 'dog', 'cat', 'pet'}
    user_input = input("Talk to me please>")
    has_question_mark = user_input.endswith("?")
    stripped_words = user_input.lower().strip(string.punctuation).split()
    match stripped_words:
        # Rule 1
        case ["bye"]:
            print(f"Bye {name}.", "\nHave a great day!")
            return True
        # Rule 2
        case [*words] if set(words) & SPECIAL_TOPICS:
            print(f"Tell me more about your "
                  f"{(set(words) & SPECIAL_TOPICS).pop()},"
                  f" {name}.")
        # Rule 3
        case [("do" | "can" | "will" | "would") as verb, "you", *words]:
            prompt_1 = f"No {name}, I {verb} not " \
                       f"{(change_person(words))}."
            prompt_2 = f"yes I {verb}."
            print(random.choice([prompt_1, prompt_2]))
        # Rule 4
        case ["why", *words] if has_question_mark:
            print("Why not?")
        # Rule 5
        case ["how", *words] if has_question_mark:
            prompt_1 = f"{name}, why do you ask?"
            prompt_2 = f"{name}, how would an answer to that help you?"
            print(random.choice([prompt_1, prompt_2]))
        # Rule 6
        case ["what", *words] if has_question_mark:
            prompt_1 = f"What do you think {name}?"
            prompt_2 = f"Why is that important {name}?"
            print(random.choice([prompt_1, prompt_2]))
        # Rule 7
        case ["i", ("need" | "think" | "have" | "want") as verb, *words]:
            print(f"Why do you {verb} "
                  f"{(change_person(words))}?")
        # Rule 8
        case ["i", *words] if words[-1] != "too":
            print(f"I {' '.join(words)} too.")
        # Rule 9
        case [("tell" | "give" | "say") as verb, *words]:
            print(f"You {verb} {' '.join(words)}.")
        # Rule 10
        case [*words] if has_question_mark:
            prompt_1 = "I have no clue."
            prompt_2 = "Maybe."
            print(random.choice([prompt_1, prompt_2]))
        # Rule 11
        case [*words] if "because" in words:
            print("Is that the real reason?")
        # Rule 12
        case _:
            prompt_1 = "That's interesting."
            prompt_2 = "That's nice!"
            prompt_3 = "Can you elaborate on that?"
            print(random.choice([prompt_1, prompt_2, prompt_3]))


def change_person(words):
    """
    Takes pronouns in words list and changes them accordingly
    :param words: list
    :return: string
    """
    PRONOUNS_DICT = {'i': 'you', 'am': 'are', 'my': 'your', 'your': 'my',
                     'me': 'you', 'you': 'me'}
    new_words = [PRONOUNS_DICT.get(word, word) for word in
                 words]
    return " ".join(new_words)


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    user_name = input("Hello. What is your name please?")
    done = chat_with(user_name)
    while not done:
        done = chat_with(user_name)


if __name__ == '__main__':
    main()
