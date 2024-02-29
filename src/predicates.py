# predicates.py

def fatci(arguments, variables):
    """
    The 'fatci' predicate always evaluates to true. It's a foundational predicate
    that asserts the existence of something.

    Args:
        arguments (list): Ignored for 'fatci' as it always returns true.
        variables (dict): The current state of variables (unused in 'fatci').

    Returns:
        bool: Always returns True.
    """
    print("fatci: True")
    return True

def sumji(arguments, variables):
    """
    The 'sumji' predicate performs addition. It expects exactly three arguments:
    the result variable, the first addend, and the second addend. If a variable
    is involved, it looks up its value in the variables dictionary.

    Args:
        arguments (list): [result_variable, addend1, addend2]
        variables (dict): Dictionary tracking variable values.

    Returns:
        bool: True if operation is successful, otherwise raises an exception.
    """
    operand1, variable_name, operand2 = arguments
    operand1_val = int(variables.get(operand1, operand1))
    operand2_val = int(variables.get(operand2, operand2))
    sum_result = operand1_val + operand2_val
    variables[variable_name] = sum_result
    print(f"{variable_name} assigned {sum_result}")
    return True

def vujni(arguments, variables):
    """
    The 'vujni' predicate performs subtraction. It requires three arguments:
    the result variable, the minuend, and the subtrahend.

    Args:
        arguments (list): [result_variable, minuend, subtrahend]
        variables (dict): Dictionary tracking variable values.

    Returns:
        int: The result of the subtraction operation.
    """
    if len(arguments) != 3:
        raise ValueError("vujni requires exactly 3 arguments.")
    try:
        subtraction_result = int(variables.get(arguments[1], arguments[1])) - int(variables.get(arguments[2], arguments[2]))
    except ValueError as e:
        raise ValueError(f"Invalid argument for vujni: {e}")
    variables[arguments[0]] = subtraction_result
    print(f"vujni({arguments}): {subtraction_result}")
    return subtraction_result

def dunli(arguments, variables):
    """
    The 'dunli' predicate checks equality between two values. It requires two arguments,
    which can be numbers, variable names, or a combination thereof.

    Args:
        arguments (list): [value1, value2]
        variables (dict): Dictionary tracking variable values.

    Returns:
        bool: True if the values are equal, False otherwise.
    """
    if len(arguments) != 2:
        raise ValueError("dunli requires exactly 2 arguments.")
    result = variables.get(arguments[0], arguments[0]) == variables.get(arguments[1], arguments[1])
    print(f"dunli({arguments}): {result}")
    return result

def steni(arguments, variables):
    """
    The 'steni' predicate sets a variable to an empty list. It requires one argument,
    the variable name to be set.

    Args:
        arguments (list): [variable_name]
        variables (dict): Dictionary tracking variable values.

    Returns:
        bool: True, indicating the variable has been set to an empty list.
    """
    if len(arguments) != 1:
        raise ValueError("steni requires exactly 1 argument.")
    variables[arguments[0]] = []
    print(f"steni({arguments}): []")
    return True

def steko(arguments, variables):
    """
    The 'steko' predicate creates a cons cell (a pair) from two values. It requires
    three arguments: the result variable, the first value, and the second value.

    Args:
        arguments (list): [result_variable, value1, value2]
        variables (dict): Dictionary tracking variable values.

    Returns:
        list: A list representing the cons cell.
    """
    if len(arguments) != 3:
        raise ValueError("steko requires exactly 3 arguments.")
    cons_cell = [variables.get(arguments[1], arguments[1]), variables.get(arguments[2], arguments[2])]
    variables[arguments[0]] = cons_cell
    print(f"steko({arguments}): {cons_cell}")
    return cons_cell

def cmavo(arguments, variables):
    """
    The 'cmavo' predicate is a simplified demonstration of declaring a new predicate
    with its arguments. It requires at least two arguments: the predicate name and
    its argument(s).

    Args:
        arguments (list): The first item is the predicate name, followed by its arguments.
        variables (dict): Dictionary tracking variable values.

    Returns:
        bool: True, indicating successful declaration of the predicate.
    """
    if len(arguments) < 2:
        raise ValueError("cmavo requires at least 2 arguments.")
    variables[arguments[0]] = arguments[1:]
    print(f"cmavo({arguments}): {arguments[1:]}")
    return True
