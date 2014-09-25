import unittest
from easy.challenge_num_nintythree import capitalize_words

class CapitalizeWordsTest(unittest.TestCase):
    """
    Capitalize the first letter in each word of a sentence
    """
    def setUp(self):
        pass

    def test_case_1(self):
        test_input = 'Hello world'
        self.assertEquals(capitalize_words(test_input),
                          'Hello World')

    def test_case_2(self):
        test_input = 'javaScript language'
        self.assertEquals(capitalize_words(test_input),
                          'JavaScript Language')

    def test_case_3(self):
        test_input = 'a letter'
        self.assertEquals(capitalize_words(test_input),
                          'A Letter')

    def test_case_4(self):
        test_input = '1st Thing'
        self.assertEquals(capitalize_words(test_input),
                          '1st Thing')

if __name__ == '__main__':
    unittest.main()