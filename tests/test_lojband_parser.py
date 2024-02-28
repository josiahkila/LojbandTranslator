import unittest
from src.logic_processor import parse_input

class TestLojbanParser(unittest.TestCase):
    
    def test_correct_parsing(self):
        expected = [('Other', 'i'), ('Other', 'lo'), ('Name', '.john.'), ('Predicate Word', 'fatci')]
        self.assertEqual(parse_input("i lo .john. fatci"), expected)
    
    def test_case_insensitivity(self):
        expected = [('Other', 'i'), ('Other', 'lo'), ('Name', '.john.'), ('Predicate Word', 'fatci')]
        self.assertEqual(parse_input("I Lo .John. Fatci"), expected)
    
    def test_whitespace_handling(self):
        expected = [('Other', 'i'), ('Other', 'lo'), ('Name', '.john.'), ('Predicate Word', 'fatci')]
        self.assertEqual(parse_input("i\tlo\n.john.\t fatci"), expected)
    
    def test_digit_handling(self):
        expected = [('Other', 'i'), ('Number', '42'), ('Predicate Word', 'fatci')]
        self.assertEqual(parse_input("i 42 fatci"), expected)
        # Test for leading zeros in a number
        with self.assertRaises(ValueError):
            parse_input("i 007 fatci")
    
    def test_period_handling(self):
    # Valid name format test
        self.assertEqual(parse_input("i lo .john.doe. fatci"), [('Other', 'i'), ('Other', 'lo'), ('Name', '.john.doe.'), ('Predicate Word', 'fatci')])
        
        # Invalid name format test - should raise ValueError
        with self.assertRaises(ValueError):
            parse_input("i lo john.doe fatci")

if __name__ == '__main__':
    unittest.main()
