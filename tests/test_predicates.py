import unittest
from src.predicates import fatci, sumji, vujni, steni, steko, cmavo, dunli

class TestPredicates(unittest.TestCase):
    def setUp(self):
        # Setup method to initialize variables for the tests
        self.variables = {}

    def test_fatci_always_true(self):
        # fatci should always return True
        self.assertTrue(fatci([], self.variables))

    def test_sumji_basic(self):
        # Testing sumji with basic addition
        arguments = ['result', '2', '3']
        sumji(arguments, self.variables)
        self.assertEqual(self.variables['result'], 5)

    def test_vujni_basic(self):
        # Testing vujni with basic subtraction
        arguments = ['result', '5', '2']
        vujni(arguments, self.variables)
        self.assertEqual(self.variables['result'], 3)

    def test_sumji_invalid_arguments(self):
        # Testing sumji with invalid number of arguments
        with self.assertRaises(ValueError):
            sumji(['result', '2'], self.variables)

    def test_vujni_invalid_arguments(self):
        # Testing vujni with invalid number of arguments
        with self.assertRaises(ValueError):
            vujni(['result'], self.variables)

    def test_dunli_equal(self):
            # Test for equality
            self.assertTrue(dunli(['5', '5'], self.variables))

    def test_dunli_not_equal(self):
        # Test for inequality
        self.assertFalse(dunli(['5', '3'], self.variables))

    def test_steni_empty_list(self):
        # Test for setting a variable to an empty list
        arguments = ['emptyList']
        steni(arguments, self.variables)
        self.assertEqual(self.variables['emptyList'], [])

    def test_steko_cons_cell(self):
        # Test for creating a cons cell
        arguments = ['myList', 'head', 'tail']
        self.variables['head'] = 'H'
        self.variables['tail'] = ['T']
        expected_cons_cell = ['H', ['T']]
        steko(arguments, self.variables)
        self.assertEqual(self.variables['myList'], expected_cons_cell)

    def test_cmavo_custom_predicate(self):
        # Placeholder test for cmavo, as its implementation depends on executing custom logic
        # This test assumes cmavo simply stores the arguments for later use
        arguments = ['customPred', 'arg1', 'arg2']
        cmavo(arguments, self.variables)
        self.assertIn('customPred', self.variables)
        self.assertEqual(self.variables['customPred'], ['arg1', 'arg2'])
        
# Adding more tests for dunli, steni, steko, cmavo as needed

if __name__ == '__main__':
    unittest.main()
