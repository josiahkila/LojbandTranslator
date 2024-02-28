# predicates.py

def fatci(arguments, variables):
    # fatci always evaluates to true
    result = True
    print(f"fatci: {result}")
    return result

def sumji(arguments, variables):
    # Assuming arguments are in the form [variable_name, addend1, addend2]
    variable_name, addend1, addend2 = arguments
    addend1_value = int(variables.get(addend1, addend1))
    addend2_value = int(variables.get(addend2, addend2))
    sum_result = addend1_value + addend2_value

    # Check if the variable already exists and has a different value
    if variable_name in variables and variables[variable_name] != sum_result:
        print(f"sumji({arguments}): Attempt to reassign '{variable_name}' to a new value {sum_result}, which is inconsistent with its existing value {variables[variable_name]}")
        return False  # Inconsistent reassignment detected

    # Otherwise, update the variable and return True
    variables[variable_name] = sum_result
    print(f"sumji({arguments}): {sum_result}")
    return True

def vujni(arguments, variables):
    # Validate the correct number of arguments for vujni
    if len(arguments) != 3:
        raise ValueError("vujni requires exactly 3 arguments.")
    # Try to convert arguments to integers safely
    try:
        subtraction_result = int(variables.get(arguments[1], arguments[1])) - int(variables.get(arguments[2], arguments[2]))
    except ValueError as e:
        raise ValueError(f"Invalid argument for vujni: {e}")
    
    variables[arguments[0]] = subtraction_result
    print(f"vujni({arguments}): {subtraction_result}")
    return subtraction_result

def dunli(arguments, variables):
    # Validate the correct number of arguments for dunli
    if len(arguments) != 2:
        raise ValueError("dunli requires exactly 2 arguments.")
    result = variables.get(arguments[0], arguments[0]) == variables.get(arguments[1], arguments[1])
    print(f"dunli({arguments}): {result}")
    return result

def steni(arguments, variables):
    # Validate the correct number of arguments for steni
    if len(arguments) != 1:
        raise ValueError("steni requires exactly 1 argument.")
    variables[arguments[0]] = []
    print(f"steni({arguments}): []")
    return True

def steko(arguments, variables):
    # Validate the correct number of arguments for steko
    if len(arguments) != 3:
        raise ValueError("steko requires exactly 3 arguments.")
    cons_cell = [variables.get(arguments[1], arguments[1]), variables.get(arguments[2], arguments[2])]
    variables[arguments[0]] = cons_cell
    print(f"steko({arguments}): {cons_cell}")
    return cons_cell

def cmavo(arguments, variables):
    # Simplified for demonstration. Real implementation would need more checks.
    if len(arguments) < 2:
        raise ValueError("cmavo requires at least 2 arguments.")
    variables[arguments[0]] = arguments[1:]
    print(f"cmavo({arguments}): {arguments[1:]}")
    return True
