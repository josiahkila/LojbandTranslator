# logic_processor.py
import re
from predicates import fatci, sumji, vujni, dunli, steni, steko, cmavo

# Maps Lojban predicate names to corresponding Python function implementations.
predicate_functions = {
    'fatci': fatci,
    'sumji': sumji,
    'vujni': vujni,
    'dunli': dunli,
    'steni': steni,
    'steko': steko,
    'cmavo': cmavo,
}

def process_lojban_statement(statement, variables):
    """
    Processes a Lojban statement, executing predicates and managing variables.
    
    Args:
        statement (str): The Lojban statement to be processed.
        variables (dict): A dictionary to store and track variables' values.
        
    Returns:
        str: A message indicating the completion of processing.
    """
    # Tokenizes the Lojban statement into identifiable parts.
    tokens = tokenize_lojban(statement)

    # Initialize control variables for predicate processing.
    predicate_name = None
    args = []
    swap_next_args = False  # Determines if arguments of the next predicate need to be swapped.

    # Iterate over each token to process predicates and their arguments.
    for token_type, token_value in tokens:
        if token_value == 'i':
            # Skip 'i', which denotes the start of a statement.
            continue

        if token_type == 'Short Word' and token_value == 'se':
            # 'se' indicates the arguments for the next predicate should be swapped.
            swap_next_args = True
            continue

        if token_type == 'Predicate Word':
            # Process any pending predicate before starting a new one.
            if predicate_name:
                process_predicate(predicate_name, args, variables, swap_next_args)
                args = []  # Reset for the next predicate.
                swap_next_args = False  # Reset the flag.

            predicate_name = token_value  # Update the current predicate name.
        else:
            # Append other tokens as arguments for the current predicate.
            args.append(token_value)

    # Ensure the last predicate is processed.
    if predicate_name:
        process_predicate(predicate_name, args, variables, swap_next_args)

    return "Lojban statement processing complete."

def process_predicate(predicate_name, args, variables, swap_next_args):
    """
    Processes a predicate with its arguments, applying any necessary argument adjustments.

    Args:
        predicate_name (str): The name of the predicate to process.
        args (list): The arguments for the predicate.
        variables (dict): The current state of variables.
        swap_next_args (bool): Whether to swap the first two arguments.
    """
    # Prepare arguments, swapping if indicated by 'se'.
    if swap_next_args and len(args) >= 2:
        args[0], args[1] = args[1], args[0]

    # Attempt to execute the predicate function with prepared arguments.
    if predicate_name in predicate_functions:
        try:
            result = predicate_functions[predicate_name](args, variables)
            print(f"Processed {predicate_name} with args {args}: Result - {result}")
        except Exception as e:
            print(f"Error processing {predicate_name}: {e}")
    else:
        print(f"Unknown predicate: {predicate_name}")

def tokenize_lojban(input_text):
    """
    Tokenizes Lojban text into identifiable tokens for processing.

    Args:
        input_text (str): The Lojban text to tokenize.

    Returns:
        list: A list of tokens identified from the input text.
    """
    input_text += ' '  # Ensure the last token is processed.
    tokens = []

    buffer = ""
    in_period_enclosed_name = False

    # Process each character in the input text.
    for char in input_text:
        if char.isalpha() or char.isdigit():
            buffer += char
        elif char == '.':
            # Handle period-enclosed names.
            if not in_period_enclosed_name:
                in_period_enclosed_name = True
                buffer += char
            else:
                if buffer:
                    tokens.append(('Name', buffer + char))
                    buffer = ""
                in_period_enclosed_name = False
        elif char.isspace():
            if buffer:
                token_type = determine_token_type(buffer)
                tokens.append((token_type, buffer))
                buffer = ""
        else:
            raise ValueError(f"Invalid character in input: {char}")

    return tokens

def determine_token_type(buffer):
    """
    Determines the type of a token based on its content.

    Args:
        buffer (str): The token content to classify.

    Returns:
        str: The classified token type.
    """
    if buffer.isdigit():
        return 'Number'
    elif len(buffer) == 1:
        return 'Short Word' if buffer != 'i' else 'Other'
    elif len(buffer) == 5:
        return 'Predicate Word'
    elif buffer.startswith('.') and buffer.endswith('.'):
        return 'Name'
    else:
        return 'Other'

def print_variables(variables):
    """
    Prints the variables and their assigned values.

    Args:
        variables (dict): The variables to print.
    """
    print("Variables and Their Values:")
    for variable, value in variables.items():
        print(f"{variable}: {value}")
