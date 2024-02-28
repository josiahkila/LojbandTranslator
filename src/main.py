from json_parser import parse_json
from logic_processor import process_logic
from predicates import fatci, sumji, vujni, dunli, steni, steko, cmavo
from src.json_parser import parse_statement

def process_lojban_statement(statement):
    # Assume parse_statement breaks down the statement into components
    parsed_statement = parse_statement(statement)
    
    # This is an example of how your parsed_statement might look after parsing
    # For simplicity, let's assume it's a list of tuples where the first element is the predicate or structure word and the second is its arguments
    # e.g., [("sumji", ["result", "2", "2"]), ("fatci", [".broda."]), ...]

    # Initialize a dictionary to store variables and their values
    variables = {}
    result = None  # Initialize result variable

    # Process each component based on your Lojban language rules
    for word, arguments in parsed_statement:
        if word == "fatci":
            result = fatci(arguments, variables)
        elif word == "sumji":
            result = sumji(arguments, variables)
        elif word == "vujni":
            result = vujni(arguments, variables)
        elif word == "dunli":
            result = dunli(arguments, variables)
        elif word == "steni":
            result = steni(arguments, variables)
        elif word == "steko":
            result = steko(arguments, variables)
        elif word == "cmavo":
            result = cmavo(arguments, variables)
        # Add more predicates as needed
        else:
            print(f"Unhandled word: {word}")

    # Return a meaningful result based on the processing
    return f"Processed statement with result: {result}"

def main():
    # User choice for JSON processing or Lojban statement processing
    choice = input("Do you want to process a JSON file (J) or a Lojban statement (L)? [J/L]: ")
    
    if choice.lower() == 'j':
        json_file_path = input("Enter the path to the JSON file: ")
        try:
            data = parse_json(json_file_path)
            print("Parsed data:", data)
            processed_data = process_logic(data)
            print("Processed data:", processed_data)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    elif choice.lower() == 'l':
        # Ask the user for a Lojban statement
        lojban_statement = input("Enter your Lojban statement: ")
        # Process the Lojban statement
        result = process_lojban_statement(lojban_statement)
        print(result)
    
    else:
        print("Invalid choice. Exiting.")

# If you have a GUI, you might conditionally start it here based on user choice

if __name__ == "__main__":
    main()
