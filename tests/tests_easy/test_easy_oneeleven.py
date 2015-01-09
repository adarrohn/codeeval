import unittest
from easy.challenge_num_oneeleven import return_longest_word

class LongestWordTest(unittest.TestCase):
    """
    Return the longest word in the line, if multiple return the first
    """
    def setUp(self):
        pass

    def test_case_all_different(self):
        """
        All words are of different lengths
        """
        self.assertEquals(return_longest_word('One Five Eleven A Seven'),
                          'Eleven')

    def test_case_all_same(self):
        """
        All words are of the same length
        """
        self.assertEquals(return_longest_word('One Two Six'),
                          'One')

    def test_case_multiple_same(self):
        """
        More than one word has the same length, but not all of them and equal
        """
        self.assertEquals(return_longest_word('One Niner Two Six Seven'),
                          'Niner')

    def test_case_one_word(self):
        """
        Only contains a single word
        """
        self.assertEquals(return_longest_word('One'),
                          'One')


if __name__ == '__main__':
    unittest.main()