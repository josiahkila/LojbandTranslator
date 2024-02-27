# logic_processor.py

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
