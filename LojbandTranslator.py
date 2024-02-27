from LojbanParser import LojbanParser

def main():
    # Initialize the parser
    parser = LojbanParser()
    
    # Read input from the user or file
    print("Enter Lojban text (type 'exit' to quit):")
    while True:
        input_text = input("> ")
        if input_text.lower() == "exit":
            break

        # Parse the input text
        try:
            result = parser.parse(input_text)
            if result is not None:
                print("Result:", result)
            else:
                print("No valid interpretation found.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
