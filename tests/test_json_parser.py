import os
import tempfile
import unittest
from src.json_parser import parse_json  # Update the import path based on your project structure

class TestJsonParser(unittest.TestCase):

    def test_parse_valid_json(self):
        # Creating a temporary file
        with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp:
            json_content = '{"name": "John", "age": 30}'
            tmp.write(json_content)
            tmp.seek(0)  # Go back to the beginning of the file after writing

            expected_result = {"name": "John", "age": 30}
            # Pass the file name instead of the JSON string
            self.assertEqual(parse_json(tmp.name), expected_result)

        # Clean up the temporary file
        os.unlink(tmp.name)

    def test_parse_invalid_json(self):
        # Creating a temporary file for invalid JSON
        with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tmp:
            tmp.write('{"name": "John", "age": 30')
            tmp.seek(0)

            # Expecting a ValueError to be raised due to invalid JSON
            with self.assertRaises(ValueError):
                parse_json(tmp.name)

        # Clean up the temporary file
        os.unlink(tmp.name)

if __name__ == '__main__':
    unittest.main()
