# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Timothy Phan and Ibrahim Dobashi
# Date: 2/20/2023
# ----------------------------------------------------------------------
"""
A program that gives the song statistics of two songs the user inputted

In this program, the user is prompted to enter two files containing song
lyrics of their choice.From there the program will take the song text
files and convert them into a word list.The program uses the word lists
to find the total words in each song and the words found in both songs
that are 4 letters or more in alphabetical order.Using the word list,
the program will create a tally dictionary of the words and the number
of times they appear in the song. Using that tally dictionary, the
program will be able to find the 8 most common words sorted by the
number of times they appear in descending order, the number of distinct
words in each song, the words that are 4-letter or longer and that
appear more than 3 times sorted alphabetically, and the longest word
in each song.
"""
import string


def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    # Enter your code below and take out the pass statement
    tally_dict = {}
    for word in words:
        if word in tally_dict:
            tally_dict[word] += 1
        else:
            tally_dict[word] = 1
    return tally_dict


def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    # Enter your code below and take out the pass statement
    desc_word_count = sorted(word_count, key=word_count.get, reverse=True)[:8]
    print("The 8 most common words are: ")
    for word in desc_word_count:
        print(f"  {word}: appears {word_count[word]} times.")


def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    # Enter your code below and take out the pass statement
    sorted_words = sorted({word for word in word_count if len(word) >= 4 and
                           word_count[word] > 3})
    print("The following (4-letter or longer) words appear more than 3 times:")
    for word in sorted_words:
        print(f"  {word}")


def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    # Enter your code below and take out the pass statement
    with open(filename, 'r', encoding='UTF-8') as input_file:
        song_read = input_file.read()
    word_list = [(word.strip(string.punctuation).lower()) for word in
                 song_read.split()]
    return word_list


def get_stats(words):
    """
    Print the statistics corresponding to the list of words specified.
    :param words: (list of strings) list of lowercase words
    :return: None
    """
    # Call the tally function to build the word count dictionary
    # Then call the appropriate functions and print:
    # 1. The eight most common words in the song in descending order of
    #    frequency, with the number of times they appear.
    # 2. The total number of words in the song.
    # 3. The number of distinct words in the song.
    # 4. The words that are 4-letter or longer and that appear more
    #    than 3 times sorted alphabetically.
    # 5. The longest word.
    words_dict = tally(words)
    most_common(words_dict)
    print(f"There are {len(words)} total words in the song.")
    print(f"There are {len(set(words_dict))} distinct words in the song.")
    repeats(words_dict)
    longest_word = max(words_dict, key=len)
    print(f"The longest word in the song is: {longest_word}")
    print("-" * 80)


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    # Enter your code below and take out the pass statement
    words1_set = set(words1)
    words2_set = set(words2)
    words = sorted({word for word in words1_set & words2_set if len(
        word) >= 4})
    print("The words (4-letter or longer) that appear in both songs:")
    for word in words:
        print(f"{word}")


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    file_list = []
    word_list = []
    for i in range(2):
        file_list.append(input(f"Please enter the filename containing song "
                               f"{i + 1}:"))
        word_list.append(get_words(file_list[i]))
    for i in range(len(word_list)):
        print(f"Song Statistics: {file_list[i]}")
        get_stats(word_list[i])
    common_words(word_list[0], word_list[1])


if __name__ == '__main__':
    main()
