import unittest
from generate_concordance.word_info import WordInfo


class TestWordInfo(unittest.TestCase):
    def test_init(self):
        actual_word_info: WordInfo = WordInfo(word_frequency=2, word_first_appearance="3")
        self.assertEqual(2, actual_word_info.word_frequency)
        self.assertEqual(list(["3"]), actual_word_info.word_appearances)

    def test_eq(self):
        word_info_left: WordInfo = WordInfo(word_frequency=2, word_first_appearance="3")
        word_info_right: WordInfo = WordInfo(word_frequency=2, word_first_appearance="3")
        self.assertEqual(word_info_left, word_info_right)


if __name__ == '__main__':
    unittest.main()
