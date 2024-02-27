import unittest
from src.logic_processor import parse_input

class TestLojbanParser(unittest.TestCase):
    
    def test_correct_parsing(self):
        self.assertEqual(parse_input("i lo .john. fatci"), ["i", "lo", ".john.", "fatci"])
    
    def test_case_insensitivity(self):
        self.assertEqual(parse_input("I Lo .John. Fatci"), ["i", "lo", ".john.", "fatci"])
    
    def test_whitespace_handling(self):
        self.assertEqual(parse_input("i\tlo\n.john.\t fatci"), ["i", "lo", ".john.", "fatci"])
    
    def test_digit_handling(self):
        self.assertEqual(parse_input("i 42 fatci"), ["i", "42", "fatci"])
        with self.assertRaises(ValueError):
            parse_input("i 007 fatci")
    
    def test_period_handling(self):
        self.assertEqual(parse_input("i lo .john.doe. fatci"), ["i", "lo", ".john.doe.", "fatci"])
        with self.assertRaises(ValueError):
            parse_input("i lo john.doe fatci")

if __name__ == '__main__':
    unittest.main()
