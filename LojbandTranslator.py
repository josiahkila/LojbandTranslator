import re
from enum import Enum
# Token types
class TokenType(Enum):
    SHORT_WORD = 1
    PREDICATE_WORD = 2
    NUMBER = 3
    NAME = 4
    ERROR = 5

# Token definition
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Scanner implementation
def scan(input_string):
    tokens = []
    words = input_string.split()
    for word in words:
        if re.match(r"^[a-z]{1,2}$", word):  # Short words
            tokens.append(Token(TokenType.SHORT_WORD, word))
        elif re.match(r"^[a-z]{5}$", word):  # Predicate words
            tokens.append(Token(TokenType.PREDICATE_WORD, word))
        elif re.match(r"^\d+$", word):  # Numbers
            tokens.append(Token(TokenType.NUMBER, int(word)))
        elif re.match(r"^\.[a-z]+\.$", word):  # Names
            tokens.append(Token(TokenType.NAME, word))
        else:
            tokens.append(Token(TokenType.ERROR, word))
    return tokens

# Parser skeleton - To be implemented based on specific rules
def parse(tokens):
    # Implementation of parsing logic based on tokens
    pass
# Simplified example of handling specific predicates
def evaluate_statement(statement):
    # Logic to evaluate statements based on predefined words and predicates
    pass

# Main execution loop
def main():
    input_string = input("Enter your code: ")
    tokens = scan(input_string)
    parsed_structure = parse(tokens)
    result = evaluate_statement(parsed_structure)
    print("Result:", result)

if __name__ == "__main__":
    main()
