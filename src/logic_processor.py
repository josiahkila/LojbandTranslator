# logic_processor.py
import re
from src.predicates import fatci, sumji, vujni, dunli, steni, steko, cmavo

def parse_input(input_text):
    input_text = input_text.lower() + ' '  # Ensure processing of the last token
    tokens = []

    buffer = ""
    in_period_enclosed_name = False

    for char in input_text:
        if char.isalpha() or char.isdigit():
            buffer += char
        elif char == '.':
            # Check for consecutive periods or start/end of a period-enclosed name
            if not buffer and not in_period_enclosed_name:
                # Starting a new name with a period
                in_period_enclosed_name = True
                buffer += char
            elif buffer and in_period_enclosed_name:
                # Ending a name with a period
                buffer += char
                tokens.append(('Name', buffer))
                print(f"Token: {buffer}, Type: Name")
                buffer = ""
                in_period_enclosed_name = False
            else:
                # Invalid usage of periods
                raise ValueError(f"Invalid period usage near: {buffer}")
        elif char.isspace():
            if buffer:
                # Process the accumulated buffer
                if buffer.isdigit():
                    # Number validation for leading zeros
                    if len(buffer) > 1 and buffer.startswith('0'):
                        raise ValueError(f"Invalid number with leading zeros: {buffer}")
                    tokens.append(('Number', buffer))
                elif len(buffer) == 1 and buffer != 'i':  # Exclude 'i'
                    tokens.append(('Short Word', buffer))
                elif len(buffer) == 5:
                    tokens.append(('Predicate Word', buffer))
                else:
                    # Generic catch-all for other tokens
                    tokens.append(('Other', buffer))
                print(f"Token: {buffer}, Type: Other")
                buffer = ""
        else:
            # Catch-all for any other characters
            raise ValueError(f"Invalid character in input: {char}")

    return tokens

def count_characters(text):
    """
    Counts the number of characters in the provided text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The total number of characters in the text.
    """
    return len(text)


def count_words(text):
    """
    Counts the number of words in the provided text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The total number of words in the text.
    """
    words = text.split()
    return len(words)


def simple_translate(text, translation_dict):
    """
    Translates words in the provided text based on a translation dictionary.

    Args:
        text (str): The text to translate.
        translation_dict (dict): A dictionary mapping words from the source language to the target language.

    Returns:
        str: The translated text.
    """
    words = text.split()
    translated_words = [translation_dict.get(word, word) for word in words]
    return ' '.join(translated_words)


# Example translation dictionary (expand according to your needs)
translation_dict = {
    'hello': 'hola',
    'world': 'mundo',
    # Add more word translations here
}

# Example usage (this part is usually not included in the module itself but shown here for demonstration)
if __name__ == "__main__":
    sample_text = "hello world"
    print("Original text:", sample_text)
    print("Character count:", count_characters(sample_text))
    print("Word count:", count_words(sample_text))
    print("Translated text:", simple_translate(sample_text, translation_dict))
