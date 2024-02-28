import unittest
from src.predicates import sumji

class TestSumji(unittest.TestCase):
    def setUp(self):
        # Initialize a dictionary to simulate the variable environment
        self.variables = {}

    def test_sumji_basic_addition(self):
        # Test basic addition
        self.assertTrue(sumji(['result', '2', '2'], self.variables))
        self.assertEqual(self.variables['result'], 4)

    def test_sumji_assign_to_variable(self):
        # Assign result to a variable and check its value
        self.assertTrue(sumji(['answer', '2', '2'], self.variables))
        self.assertEqual(self.variables['answer'], 4)

    def test_sumji_use_variable_in_addition(self):
        # Use a previously assigned variable in a new sumji operation
        self.variables['answer'] = 4
        self.assertTrue(sumji(['newAnswer', '40', '2'], self.variables))
        self.assertEqual(self.variables['newAnswer'], 42)

    def test_sumji_assign_variable_inconsistent_value(self):
        # Setup: Define 'brook' with an initial value
        self.variables['brook'] = 55
        # Test: Attempt to reassign 'brook' to an inconsistent new value
        result = sumji(['brook', '5', '5'], self.variables)
        self.assertFalse(result, "sumji should return False when trying to reassign a variable to an inconsistent value.")
        self.assertEqual(self.variables['brook'], 55, "The value of 'brook' should remain unchanged after an attempted inconsistent reassignment.")

    def test_sumji_assign_variable_consistent_value(self):
        # Correctly assign a new value to an existing variable
        self.variables['brook'] = 55
        self.assertTrue(sumji(['brook', '50', '5'], self.variables))
        self.assertEqual(self.variables['brook'], 55)

if __name__ == '__main__':
    unittest.main()
