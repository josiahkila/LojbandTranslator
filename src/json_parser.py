import json

def parse_json(file_path):
    """
    Parses a JSON file and returns the data.
    
    Parameters:
    - file_path: str, the path to the JSON file to be parsed.
    
    Returns:
    - The parsed JSON data as a Python dictionary.
    
    Raises:
    - ValueError: If the JSON file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from the file {file_path}: {e}")

