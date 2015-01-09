import unittest
from easy.challenge_num_onetwelve import swap_elements


class ElementSwapTest(unittest.TestCase):
    """

    """
    def setUp(self):
        pass

    def test_case_single_swap(self):
        """
        Swap one elements position

        """
        self.assertEquals(swap_elements('1 2 3 4 5 6 7 8 9 : 0-8'),
                          '9 2 3 4 5 6 7 8 1')

    def test_case_multiple_swap(self):
        """
        Perform two element position swaps
        """
        self.assertEquals(swap_elements('1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3'),
                          '2 4 3 1 5 6 7 8 9 10')


if __name__ == '__main__':
    unittest.main()