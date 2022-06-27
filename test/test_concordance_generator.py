import unittest
from typing import Dict, List

from generate_concordance.concordance_generator import ConcordanceGenerator
from generate_concordance.word_info import WordInfo


class TestConcordanceGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.concordance_generator = ConcordanceGenerator()

        self.expected_longest_word: int = len("sentence")

        a_word_info: WordInfo = WordInfo(2, "1")
        a_word_info.word_appearances.append("2")
        test_word_info: WordInfo = WordInfo(2, "1")
        test_word_info.word_appearances.append("2")

        self.expected_word_to_info: Dict[str, WordInfo] = dict({"this": WordInfo(1, "1"),
                                                                "is": WordInfo(1, "1"),
                                                                "a": a_word_info,
                                                                "simple": WordInfo(1, "1"),
                                                                "test": test_word_info,
                                                                "two": WordInfo(1, "2"),
                                                                "sentence": WordInfo(1, "2")})

    def test_init(self):
        self.assertIsNone(self.concordance_generator.get_longest_word())
        self.assertIsNone(self.concordance_generator.get_word_to_info())

    def test_get_longest_word(self):
        self.concordance_generator.generate_concordance("This is a simple test. A two sentence test.")
        self.assertEqual(self.expected_longest_word, self.concordance_generator.get_longest_word())

    def test_get_word_to_info(self):
        self.concordance_generator.generate_concordance("This is a simple test. A two sentence test.")
        actual_word_to_info: Dict[str, WordInfo] = self.concordance_generator.get_word_to_info()
        self.assertDictEqual(self.expected_word_to_info, actual_word_to_info)

    def test_generate_concordance(self):
        self.concordance_generator.generate_concordance("This is a simple test. A two sentence test.")

        expected_largest_word: int = 8

        self.assertEqual(expected_largest_word, self.concordance_generator.get_longest_word())

        actual_word_to_info: Dict[str, WordInfo] = self.concordance_generator.get_word_to_info()
        self.assertDictEqual(self.expected_word_to_info, actual_word_to_info)

    def test_get_concordance_lines(self):
        self.concordance_generator.generate_concordance("This is a simple test. A two sentence test.")
        actual_lines: List[str] = list(["a. a        {2:1,2}",
                                        "b. is       {1:1}",
                                        "c. sentence {1:2}",
                                        "d. simple   {1:1}",
                                        "e. test     {2:1,2}",
                                        "f. this     {1:1}",
                                        "g. two      {1:2}"])

        self.assertEqual(actual_lines, self.concordance_generator.get_concordance_lines())


if __name__ == '__main__':
    unittest.main()
