import unittest

from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value, find_optimal, combinations

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

class TestWordValue(unittest.TestCase):

    def test_load_words(self):
        words = load_words()
        self.assertEqual(len(words), 235886)
        self.assertEqual(words[0], 'A')
        self.assertEqual(words[-1], 'Zyzzogeton')
        self.assertNotIn(' ', ''.join(words))

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('bob'), 7)
        self.assertEqual(calc_word_value('JuliaN'), 13)
        self.assertEqual(calc_word_value('PyBites'), 14)
        self.assertEqual(calc_word_value('benzalphenylhydrazone'), 56)

    def test_max_word_value(self):
        self.assertEqual(max_word_value(TEST_WORDS), 'barbeque')
        self.assertEqual(max_word_value(), 'benzalphenylhydrazone')

    def test_find_optimal(self):
        self.assertEqual(find_optimal('pplea'),('apple',9))
        self.assertEqual(find_optimal('ppleaa'),('apple',9))

if __name__ == "__main__":
    print(find_optimal('ppleaa'))
    unittest.main()
