import unittest
import tkinter as tk
from src.gui import TranslatorApp

class TestTranslatorApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = TranslatorApp(self.root)
        # Prevent the main Tkinter loop from blocking the tests
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def test_widgets_exist(self):
        """Test that all widgets are created."""
        self.assertIsInstance(self.app.txt_input, tk.scrolledtext.ScrolledText, "Input text widget does not exist.")
        self.assertIsInstance(self.app.btn_char_count, tk.Button, "Character count button does not exist.")
        self.assertIsInstance(self.app.btn_word_count, tk.Button, "Word count button does not exist.")
        self.assertIsInstance(self.app.btn_translate, tk.Button, "Translate button does not exist.")
        self.assertIsInstance(self.app.lbl_result, tk.Label, "Result label does not exist.")

    def test_display_char_count(self):
        """Test the character count functionality."""
        test_text = "Hello world!"
        self.app.txt_input.insert(tk.END, test_text)
        self.app.display_char_count()
        expected_result = f"Character Count: {len(test_text)}"
        actual_result = self.app.lbl_result.cget("text")
        self.assertEqual(expected_result, actual_result, "Character count does not match expected result.")

    def test_display_word_count(self):
        """Test the word count functionality."""
        test_text = "Hello world from the test!"
        self.app.txt_input.insert(tk.END, test_text)
        self.app.display_word_count()
        expected_result = "Word Count: 5"  # Change according to your count_words logic
        actual_result = self.app.lbl_result.cget("text")
        self.assertEqual(expected_result, actual_result, "Word count does not match expected result.")

    def test_display_translation(self):
        """Test the translation functionality."""
        # Assuming the simple_translate function works as expected
        test_text = "hello world"
        self.app.txt_input.insert(tk.END, test_text)
        self.app.display_translation()
        expected_result = "Translated Text: hola mundo"  # Adjust based on your translation logic and dictionary
        actual_result = self.app.lbl_result.cget("text")
        self.assertEqual(expected_result, actual_result, "Translation does not match expected result.")

if __name__ == '__main__':
    unittest.main()
