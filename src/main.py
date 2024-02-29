from logic_processor import process_lojban_statement, print_variables

def main():
    # Your existing setup for processing Lojban statements
    lojban_statement = input("Enter your Lojban statement: ")
    variables = {}  # Assuming your process_lojban_statement function updates this dictionary
    result = process_lojban_statement(lojban_statement, variables)  # Make sure your function is designed to update 'variables'
    print(result)
    print_variables(variables)

if __name__ == "__main__":
    main()
