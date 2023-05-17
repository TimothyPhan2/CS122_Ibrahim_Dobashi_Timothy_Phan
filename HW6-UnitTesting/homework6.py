# ----------------------------------------------------------------------
# Name: Homework 6
# Purpose: implement 2 functions final_grade and most_words
# Author(s):Timothy Phan & Ibrahim Dobashi
# Date: 3/19/2023
# ----------------------------------------------------------------------
"""
Writing test cases for two functions final_grade and most_words
In this python program, we are testing two functions final_grade and
most_words. In order to test the functions, test cases need to be
made. There will be a total of 2 test cases, the final_grade test case
has 4 test methods and the most_words test cases has 3 test methods.
"""


def final_grade(student_grades, extra_credit=1):
    """
    Returns new dictionary with the students' names and their new grades
    :param student_grades: dictionary
    :param extra_credit: integer
    :return: dictionary
    """
    return {student: student_grades[student] + extra_credit for student in
            student_grades}


def most_words(*args):
    """
    Returns the string with the most words
    :param args: (string) 0 or more required parameters
    :return: string
    """
    if not args:
        return None
    return max(args, key=lambda string: len(string.split()))
