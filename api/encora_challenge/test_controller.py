import unittest
from encora_challenge.controllers import CommonWordsUsedController

class TestCommonWordsUsedController(unittest.TestCase):
    def test_common_words_count(self):
        text = "This is a test. It is only a test."
        common_words = ["is", "a", "it"]

        result = CommonWordsUsedController(text, common_words)

        expected = {
            "is": 2,
            "a": 2,
            "it": 1
        }

        self.assertEqual(result, expected)

    def test_no_common_words(self):
        text = "This is a test. It is only a test."
        common_words = ["not", "in", "text"]

        result = CommonWordsUsedController(text, common_words)

        expected = {}

        self.assertEqual(result, expected)

    def test_empty_text(self):
        text = ""
        common_words = ["is", "a", "it"]

        result = CommonWordsUsedController(text, common_words)

        expected = {}

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
