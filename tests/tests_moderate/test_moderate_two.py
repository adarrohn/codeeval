import unittest
from moderate.challenge_num_two import n_longest_lines


class NLongestLineTest(unittest.TestCase):
    """
    Given a list of elements [N, a,b, c, d], return the N longest elements
    """
    def setUp(self):
        pass

    def test_n_longest_lines(self):
        test_input = ['2',
                      'Hello World',
                      'CodeEval',
                      'Quick Fox',
                      'A',
                      'San Francisco']

        self.assertEquals(n_longest_lines(test_input),
                          ['San Francisco',
                          'Hello World'])


if __name__ == '__main__':
    unittest.main()