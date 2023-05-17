import unittest
import homework6


class FinalGradeTestCase(unittest.TestCase):
    def setUp(self):
        self.dictionary = {"John": 90, "Larry": 20, "Cindy": 55, "Harry": 100}
        self.extra_credit = 20
        self.empty_dict = {}

    def test_final_grade_default(self):
        """Test the final_grade function with the default extra-credit"""
        actual = homework6.final_grade(self.dictionary)
        expected = {"John": 91, "Larry": 21, "Cindy": 56, "Harry": 101}
        self.assertEqual(actual, expected)

    def test_final_grade_empty(self):
        """Test the final_grade function on an empty dictionary"""
        self.assertEqual(self.empty_dict, {})

    def test_final_grade_not_empty(self):
        """Test the final_grade function on a non_empty dictionary"""
        actual = homework6.final_grade(self.dictionary, self.extra_credit)
        expected = {"John": 110, "Larry": 40, "Cindy": 75, "Harry": 120}
        self.assertEqual(actual, expected)

    def test_final_grade_original(self):
        """Test if the original dictionary has not been affected"""
        actual = homework6.final_grade(self.dictionary, self.extra_credit)
        same_dict = {"John": 90, "Larry": 20, "Cindy": 55, "Harry": 100}
        self.assertEqual(self.dictionary, same_dict)


class MostWordsTestCase(unittest.TestCase):
    def test_most_words_no_args(self):
        """Test the most_words function with no arguments"""
        actual = homework6.most_words()
        self.assertIsNone(actual)

    def test_most_words_one_args(self):
        """Test the most_words function with 1 argument"""
        actual = homework6.most_words("Blueberry")
        self.assertEqual(actual, "Blueberry")

    def test_most_words_many_args(self):
        """Test the most_words function with many arguments"""
        actual = homework6.most_words("Jackal", "Cow", "dog", "atrocious",
                                      "precocious",
                                      "restroom", "balcony",
                                      "hyper active running",
                                      "winter", "vinland saga", "one piece")
        self.assertEqual(actual, "hyper active running")


if __name__ == '__main__':
    unittest.main()
