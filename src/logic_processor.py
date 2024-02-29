# logic_processor.py
import re
from predicates import fatci, sumji, vujni, dunli, steni, steko, cmavo

predicate_functions = {
    'fatci': fatci,
    'sumji': sumji,
    'vujni': vujni,
    'dunli': dunli,
    'steni': steni,
    'steko': steko,
    'cmavo': cmavo,
    # Add more mappings as needed
}

def process_lojban_statement(statement, variables):
    # The 'variables' dictionary is now passed in as an argument
    tokens = tokenize_lojban(statement)  # Tokenize the input statement correctly

    # Initialize control variables
    predicate_name = None
    args = []
    swap_next_args = False  # Flag to indicate if the next predicate's arguments should be swapped

    for token_type, token_value in tokens:
        if token_value == 'i':
            continue  # Skip the initial 'i', denoting the start of a statement

        if token_type == 'Short Word' and token_value == 'se':
            swap_next_args = True
            continue  # 'se' indicates argument swap for the next predicate; it's not an argument itself

        if token_type == 'Predicate Word':
            # Before processing the new predicate, check if there's a previous predicate to process
            if predicate_name:
                process_predicate(predicate_name, args, variables, swap_next_args)
                args = []  # Reset arguments for the next predicate
                swap_next_args = False  # Reset the swap flag after processing

            predicate_name = token_value  # Update the current predicate
        else:
            # Append other tokens as arguments (excluding 'se')
            args.append(token_value)

    # Process the last predicate in the statement
    if predicate_name:
        process_predicate(predicate_name, args, variables, swap_next_args)

    return "Lojban statement processing complete."

def process_predicate(predicate_name, args, variables, swap_next_args):
    # Initialize a list to hold the resolved arguments for the predicate
    resolved_args = []

    # Track whether the next argument should be treated as a variable name due to 'lo'
    next_arg_is_variable = False

    for arg in args:
        if arg == 'lo':
            next_arg_is_variable = True  # The next argument should be treated as a variable name
            continue
        elif arg == 'se' and not swap_next_args:
            swap_next_args = True  # Indicate that the next two arguments should be swapped
            continue

        if next_arg_is_variable:
            if arg.startswith('.'):  # Ensure it's a properly formatted variable name
                # Attempt to resolve the variable's value
                resolved_value = variables.get(arg, "UNDEFINED")
                if resolved_value == "UNDEFINED":
                    print(f"Warning: Variable {arg} is not defined.")
                resolved_args.append(resolved_value)
            next_arg_is_variable = False  # Reset for the next argument
        else:
            resolved_args.append(arg)  # Directly append if not a variable

    # Apply argument swapping if required by 'se'
    if swap_next_args and len(resolved_args) >= 2:
        resolved_args[0], resolved_args[1] = resolved_args[1], resolved_args[0]

    # Process the predicate with resolved and potentially swapped arguments
    if predicate_name in predicate_functions:
        try:
            # Attempt to process the predicate with the resolved arguments
            result = predicate_functions[predicate_name](resolved_args, variables)
            print(f"Processed {predicate_name} with args {resolved_args}: Result - {result}")
        except Exception as e:  # Catch more general exception if needed
            print(f"Error processing {predicate_name}: {e}")
    else:
        print(f"Unknown predicate: {predicate_name}")

def tokenize_lojban(input_text):
    input_text += ' '  # Ensure processing of the last token
    tokens = []

    buffer = ""
    in_period_enclosed_name = False

    for char in input_text:
        if char.isalpha() or char.isdigit():
            buffer += char
        elif char == '.':
            if not in_period_enclosed_name:
                in_period_enclosed_name = True
                buffer += char
            else:
                if buffer:  # Ensure buffer is not empty before appending
                    tokens.append(('Name', buffer + char))
                    buffer = ""
                in_period_enclosed_name = False
        elif char.isspace():
            if buffer:
                # Determine token type based on buffer content and specific rules
                token_type = determine_token_type(buffer)
                tokens.append((token_type, buffer))
                buffer = ""
        else:
            raise ValueError(f"Invalid character in input: {char}")

    return tokens

def determine_token_type(buffer):
    # Placeholder logic to determine the token type
    if buffer.isdigit():
        return 'Number'
    elif len(buffer) == 1:
        return 'Short Word' if buffer != 'i' else 'Other'  # Special handling for 'i'
    elif len(buffer) == 5:
        return 'Predicate Word'
    elif buffer.startswith('.') and buffer.endswith('.'):
        return 'Name'
    else:
        return 'Other'
    
def print_variables(variables):
    print("Predicate Words and Their Values:")
    for variable, value in variables.items():
        print(f"{variable}: {value}")
