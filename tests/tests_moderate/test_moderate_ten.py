import unittest
from moderate.challenge_num_ten import mth_last


class MthToLastTest(unittest.TestCase):
    """
    Given a string a,b,c,d,M, return the Mth last element of the list
    """
    def setUp(self):
        pass

    def test_print_mth_to_last_case_1(self):
        test_string = 'a b c d 4'

        self.assertEquals(mth_last(test_string), 'a')

    def test_print_mth_to_last_case_2(self):
        test_string = 'e f g h 2'

        self.assertEquals(mth_last(test_string), 'g')

    def test_print_mth_to_last_case_out_of_bounds(self):
        '''
        Return None in out of bounds
        '''
        test_string = 'e f g h 6'

        self.assertEquals(mth_last(test_string), None)

if __name__ == '__main__':
    unittest.main()