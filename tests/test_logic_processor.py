import unittest
from src.logic_processor import count_characters, count_words, simple_translate

class TestLogicProcessor(unittest.TestCase):

    def test_count_characters(self):
        self.assertEqual(count_characters("hello world"), 11)
        self.assertEqual(count_characters(""), 0)
        self.assertEqual(count_characters(" "), 1)

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("This is a test."), 4)

    def test_simple_translate(self):
        translation_dict = {'hello': 'hola', 'world': 'mundo'}
        self.assertEqual(simple_translate("hello", translation_dict), 'hola')
        self.assertEqual(simple_translate("world", translation_dict), 'mundo')
        self.assertEqual(simple_translate("unknown", translation_dict), 'unknown') # Assuming it returns the original word if not found

if __name__ == '__main__':
    unittest.main()
