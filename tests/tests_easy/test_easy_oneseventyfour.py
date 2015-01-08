import unittest
from easy.challenge_num_oneseventyfour import replace_with_slang


class ReplaceEveryOtherPunctuation(unittest.TestCase):
    """
    Replace every other ending punctuation mark with one of the phrases:

    ', yeah!',
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo.',
    '? No way!',
    '. Awesome!'
    """

    def setUp(self):
        self.input = (
            'Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani utroque recteque has, sea ne fugit verterem!',
            'Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu.',
            'Eu nam nusquam quaestio principes.')
        self.expected = (
            'Lorem ipsum dolor sit amet. Mea et habeo doming praesent, yeah! Te inani utroque recteque has, sea ne fugit verterem!',
            'Usu ei scripta phaedrum, an sed salutatus definiebas, this is crazy, I tell ya. Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu, can U believe this?',
            'Eu nam nusquam quaestio principes.')


    def test_case_1(self):
        self.assertEquals(replace_with_slang(self.input[0]),
                          self.expected[0])


    def test_case_2(self):
        self.assertEquals(replace_with_slang(self.input[1]),
                          self.expected[1])


    def test_case_3(self):
        self.assertEquals(replace_with_slang(self.input[2]),
                          self.expected[2])


if __name__ == '__main__':
    unittest.main()